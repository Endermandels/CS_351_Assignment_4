# Bitmap Indexing and Compression

Elijah Delavar

## Running

Make sure to put mybitmap.py in the same directory as the python file using mybitmap.py.

Indexing:
    from mybitmap import create_index
    create_index(input_file, output_path, sorted)

    # input_file:   input data file
    # output_path:  directory to store resulting index
    # sorted:       whether the data is sorted

Compressing:
    from mybitmap import compress_index
    compress_index(bitmap_index, output_path, compression_method, word_size)

    # bitmap_index:         bitmap index file
    # output_path:          directory to store resulting compressed index
    # compression_method:   WAH, BBC, PLWAH, etc. (only WAH is implemented currently)
    # word_size:            size of word
