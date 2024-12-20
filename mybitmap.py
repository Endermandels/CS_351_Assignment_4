"""
Assignment 4
Elijah Delavar
CS 351

This file creates and compresses bitmap indexes over data files of the structure: animal,age,adopted
The compression methods used a window to compress the data
"""

import sys

def matches(expr: bool):
	return '1' if expr else '0'

def parse_row(row: str):
	"""
	Takes a row from a data file and converts it to bits.
	"""
	ANIMAL = ['cat', 'dog', 'turtle', 'bird']
	AGE = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
	ADOPTED = ['True', 'False']

	segments = row.strip().split(',')
	parsed = ''
	found_age = False

	for a in ANIMAL:
		parsed += matches(segments[0] == a)

	for a in AGE:
		parsed += matches(not found_age and int(segments[1]) <= a)
		if not found_age and int(segments[1]) <= a:
			found_age = True

	for a in ADOPTED:
		parsed += matches(segments[2] == a)

	return parsed + '\n'

def create_index(input_file, output_path, sorted):
	output_file = ''
	fn = input_file.split('/')[-1]

	if sorted:
		output_file = f"{output_path}/{fn}_sorted"
	else:
		output_file = f"{output_path}/{fn}"

	try:
		with open(input_file, 'r') as infile:
			try:
				with open(output_file, 'w') as outfile:

					row = infile.readline()
					while row:
						outfile.write(parse_row(row))
						row = infile.readline()

			except Exception as e:
				print(f"Error while trying to write to '{output_file}':", e)
				sys.exit(1)
	except Exception as e:
		print(f"Error while trying to read from '{input_file}':", e)
		sys.exit(1)

def run_to_str(bit: str, bucket: list, word_size: int):
	"""
	Write a run of <bit>'s to file.
	Modifies the 0th and 2nd indeces of bucket.
	"""

	bin_str = '{0:b}'.format(bucket[0][bit])
	bucket[2] += '1' + bit + '0'*(word_size-2-len(bin_str)) + bin_str
	bucket[0][bit] = 0

def flush_buckets(buckets, word_size, rows_read):
	"""
	Transfer any runs to the string to output.
	If rows_read is greater than 0, pad the rest of the output strings.
	"""
	for bucket in buckets:
		if bucket[0]['1'] > 0:
			# Write run of 1's to file, then store run of 0's
			run_to_str('1', bucket, word_size)

		elif bucket[0]['0'] > 0:
			# Write run of 0's to file, then store run of 1's
			run_to_str('0', bucket, word_size)

		if rows_read > 0:
			# Pad with 0's to the right and add literal
			bucket[2] += '0' + bucket[3] + '0'*(word_size-1-rows_read)

def modify_buckets(buckets, word_size):
	"""
	Buckets keep track of each column's runs/literals.
	The first value in each bucket indicates how many runs of which bit have been encountered.
	The next <word_size>-1 values are the encountered bits.
	When <word_size>-1 values have been read in, check if the stored bits are a literal.
		If it is, check if the first value is a run, and write it to file if so.
	Write the literal to file.
	Empty bucket (after first value).
	"""
	for bucket in buckets:
		if bucket[1]['0']:
			if bucket[0]['1'] > 0:
				# Write run of 1's to file, then store run of 0's
				run_to_str('1', bucket, word_size)

			elif bucket[0]['0'] == 2**(word_size-2)-1:
				# Too many runs for one compressed word
				run_to_str('0', bucket, word_size)

			bucket[0]['0'] += 1

		elif bucket[1]['1']:
			if bucket[0]['0'] > 0:
				# Write run of 0's to file, then store run of 1's
				run_to_str('0', bucket, word_size)

			elif bucket[0]['1'] == 2**(word_size-2)-1:
				# Too many runs for one compressed word
				run_to_str('1', bucket, word_size)

			bucket[0]['1'] += 1

		else:
			# Encountered Literal
			if bucket[0]['1'] > 0:
				# Write run of 1's to file, then store run of 0's
				run_to_str('1', bucket, word_size)

			elif bucket[0]['0'] > 0:
				# Write run of 0's to file, then store run of 1's
				run_to_str('0', bucket, word_size)

			bucket[2] += '0' + bucket[3]

		bucket[3] = ''
		bucket[1]['0'] = 1
		bucket[1]['1'] = 1

def compress_index(bitmap_index, output_path, compression_method, word_size):
	COLUMNS = 16 # Total number of columns in bitmap
	output_file = ''
	fn = bitmap_index.split('/')[-1]
	output_file = f"{output_path}/{fn}_{compression_method}_{str(word_size)}"

	# First dict: number and type of runs
	# Second dict: whether the bits read in are a run and what type they are
	# First string: bits to output
	# Second string: bits read in
	buckets = []
	for i in range(COLUMNS):
		buckets.append([{'0': 0, '1': 0}, {'0': 1, '1': 1}, '', ''])

	try:
		with open(bitmap_index, 'r') as infile:
			try:
				with open(output_file, 'w') as outfile:

					rows_read = 0
					bindex = 0
					bit = infile.read(1)
					while bit:
						if bit == '0':
							# Add bit to correct column
							buckets[bindex][1]['1'] = 0
							buckets[bindex][3] += bit
							bindex += 1
						elif bit == '1':
							# Add bit to correct column
							buckets[bindex][1]['0'] = 0
							buckets[bindex][3] += bit
							bindex += 1
						elif bindex > 0: # Waits until a '1' or '0' is found
							rows_read += 1
							if rows_read == word_size-1:
								modify_buckets(buckets, word_size)
								rows_read = 0
							bindex = 0

						bit = infile.read(1)

					flush_buckets(buckets, word_size, rows_read)

					for bucket in buckets:
						outfile.write(bucket[2] + '\n')

			except Exception as e:
				print(f"Error while trying to write to '{output_file}':", e)
				sys.exit(1)
	except Exception as e:
		print(f"Error while trying to read from '{bitmap_index}':", e)
		sys.exit(1)

def main():
	argc = len(sys.argv)
	if argc < 2:
		print('usage: python3 mybitmap.py <index> <input_file> <output_path> <sorted>')
		print('usage: python3 mybitmap.py <compress> <input_file> <output_path> ' \
			+ '<compression_method> <word_size>')
		sys.exit(1)

	i_or_c = sys.argv[1].lower()

	if i_or_c == 'i' or i_or_c == 'index':
		if argc != 5:
			print('usage: python3 mybitmap.py <index> <input_file> <output_path> ' \
				+ '<sorted>')
			sys.exit(1)

		is_sorted = sys.argv[4].lower()

		if is_sorted == 't':
			SORTED = '_sorted'
		elif is_sorted != 'f':
			print("sorted should be either 't' or 'f'")
			sys.exit(1)

		create_index(	sys.argv[2],
				sys.argv[3],
				is_sorted == 't')

	elif i_or_c == 'c' or i_or_c == 'compress':
		if argc != 6:
			print('usage: python3 mybitmap.py <compress> <input_file> <output_path> ' \
				+ '<compression_method> <word_size>')
			sys.exit(1)

		c_method = sys.argv[4]

		if c_method == 'WAH':
			compress_index(	sys.argv[2],
					sys.argv[3],
					c_method,
					int(sys.argv[5]))

		elif c_method == 'BBC':
			print('Please use WAH for the compression_method')
			sys.exit(1)

		else:
			print('Please specify one of the following compression methods: ' \
				+ 'BBC, WAH')
			sys.exit(1)

	else:
		print("Error: Unspecified Index or Compression: Specify by typing 'i'/'index' or " \
			+ "'c'/'compression'")
		sys.exit(1)

if __name__ == '__main__':
	main()
