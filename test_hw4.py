from mybitmap import *
# import pytest

def cmp_files(file1, file2):
    with open(file1, "r") as f1:
        content1 = f1.readlines()
    with open(file2, "r") as f2:
        content2 = f2.readlines() 
    return content1 == content2

#=========================================================================================
#                                  Bitmap Index Creation
#=========================================================================================
def test_index():
    create_index("./data/data/animals.txt", "./output/bitmaps", False)
    assert cmp_files("./data/data/bitmaps/animals", "./output/bitmaps/animals.txt")

def test_index_small():
    create_index("./data/data/animals_small.txt", "./output/bitmaps", False)
    assert cmp_files("./data/data/bitmaps/animals_small", "./output/bitmaps/animals_small.txt")

def test_index_sorted():
    create_index("./data/data/animals_sorted.txt", "./output/bitmaps", True)
    assert cmp_files("./data/data/bitmaps/animals_sorted", "./output/bitmaps/animals_sorted.txt_sorted")

#=========================================================================================
#                              BBC Test (Extra Credit Only!!)
#=========================================================================================
# def test_bbc_8():
#     compress_index("./output/bitmaps/animals.txt","./output/compressed","BBC",8)
#     assert cmp_files("./mine/mine/compressed/animals_BBC_8", "./output/compressed/animals.txt_BBC_8")

# def test_bbc_8_small():
#     compress_index("./output/bitmaps/animals_small.txt","./output/compressed","BBC",8)
#     assert cmp_files("./data/data/compressed/animals_small_BBC_8", "./output/compressed/animals_small.txt_BBC_8")

# def test_bbc_8_sorted():
#     compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","BBC",8)
#     assert cmp_files("./data/data/compressed/animalSorted_sorted_BBC_8", "./output/compressed/animals_sorted.txt_sorted_BBC_8")

#=========================================================================================
#                                   WAH (animals_small)
#=========================================================================================
def test_wah_8_small():
    compress_index("./output/bitmaps/animals_small.txt","./output/compressed","WAH",8)
    assert cmp_files("./data/data/compressed/animals_small_WAH_8", "./output/compressed/animals_small.txt_WAH_8")

def test_wah_16_small():
    compress_index("./output/bitmaps/animals_small.txt","./output/compressed","WAH",16)
    assert cmp_files("./data/data/compressed/animals_small_WAH_16", "./output/compressed/animals_small.txt_WAH_16")

def test_wah_32_small():
    compress_index("./output/bitmaps/animals_small.txt","./output/compressed","WAH",32)
    assert cmp_files("./data/data/compressed/animals_small_WAH_32", "./output/compressed/animals_small.txt_WAH_32")

def test_wah_64_small():
    compress_index("./output/bitmaps/animals_small.txt","./output/compressed","WAH",64)
    assert cmp_files("./data/data/compressed/animals_small_WAH_64", "./output/compressed/animals_small.txt_WAH_64")

#=========================================================================================
#                                       WAH (animals)
#========================================================================================= 
def test_wah_4():
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",4)
    assert cmp_files("./mine/mine/compressed/animals_WAH_4", "./output/compressed/animals.txt_WAH_4")    

def test_wah_8():
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",8)
    assert cmp_files("./mine/mine/compressed/animals_WAH_8", "./output/compressed/animals.txt_WAH_8")

def test_wah_16():
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",16)
    assert cmp_files("./mine/mine/compressed/animals_WAH_16", "./output/compressed/animals.txt_WAH_16")

def test_wah_32():
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",32)
    assert cmp_files("./mine/mine/compressed/animals_WAH_32", "./output/compressed/animals.txt_WAH_32")

def test_wah_64():
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",64)
    assert cmp_files("./mine/mine/compressed/animals_WAH_64", "./output/compressed/animals.txt_WAH_64")

#=========================================================================================
#                                    WAH (animals sorted)
#========================================================================================= 
def test_wah_4_sorted():
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",4)
    assert cmp_files("./mine/mine/compressed/animalsSorted_sorted_WAH_4", "./output/compressed/animals_sorted.txt_sorted_WAH_4")

def test_wah_8_sorted():
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",8)
    assert cmp_files("./mine/mine/compressed/animalsSorted_sorted_WAH_8", "./output/compressed/animals_sorted.txt_sorted_WAH_8")

def test_wah_16_sorted():
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",16)
    assert cmp_files("./mine/mine/compressed/animalsSorted_sorted_WAH_16", "./output/compressed/animals_sorted.txt_sorted_WAH_16")

def test_wah_32_sorted():
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",32)
    assert cmp_files("./mine/mine/compressed/animalsSorted_sorted_WAH_32", "./output/compressed/animals_sorted.txt_sorted_WAH_32")

def test_wah_64_sorted():
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",64)
    assert cmp_files("./mine/mine/compressed/animalsSorted_sorted_WAH_64", "./output/compressed/animals_sorted.txt_sorted_WAH_64")

def main():
    test_index()
    test_index_small()
    test_index_sorted()

    test_wah_8_small()
    test_wah_16_small()
    test_wah_32_small()
    test_wah_64_small()

    test_wah_4()
    test_wah_8()
    test_wah_16()
    test_wah_32()
    test_wah_64()

    test_wah_4_sorted()
    test_wah_8_sorted()
    test_wah_16_sorted()
    test_wah_32_sorted()
    test_wah_64_sorted()

if __name__=="__main__":
    main()