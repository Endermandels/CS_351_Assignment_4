import sys

def matches(expr):
	"""
	If expr is True, return '1'.
	Otherwise, return '0'.
	"""
	if expr:
		return '1'
	return '0'

def parse_row(row):
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

def compress_index(bitmap_index, output_path, compression_method, word_size):
	COLUMNS = 16 # Total number of columns in bitmap
	output_file = ''
	fn = bitmap_index.split('/')[-1]
	output_file = f"{output_path}/{fn}_{compression_method}_{str(word_size)}"

	print(output_file)

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

		compress_index(	sys.argv[2],
				sys.argv[3],
				sys.argv[4],
				int(sys.argv[5]))
	else:
		print("Error: Unspecified Index or Compression: Specify by typing 'index' or " \
			+ "'compression'")
		sys.exit(1)

if __name__ == '__main__':
	main()
