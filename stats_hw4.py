from mybitmap import *
import time
import inspect
import os

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
    t0 = time.time()
    create_index("./data/data/animals.txt", "./output/bitmaps", False)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/bitmaps/animals.txt")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./data/data/bitmaps/animals", "./output/bitmaps/animals.txt")

def test_index_small():
    t0 = time.time()
    create_index("./data/data/animals_small.txt", "./output/bitmaps", False)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/bitmaps/animals_small.txt")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./data/data/bitmaps/animals_small", "./output/bitmaps/animals_small.txt")

def test_index_sorted():
    t0 = time.time()
    create_index("./data/data/animals_sorted.txt", "./output/bitmaps", True)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/bitmaps/animals_sorted.txt_sorted")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./data/data/bitmaps/animals_sorted", "./output/bitmaps/animals_sorted.txt_sorted")

#=========================================================================================
#                                   WAH (animals_small)
#=========================================================================================
def test_wah_8_small():
    t0 = time.time()
    compress_index("./output/bitmaps/animals_small.txt","./output/compressed","WAH",8)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals_small.txt_WAH_8")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./data/data/compressed/animals_small_WAH_8", "./output/compressed/animals_small.txt_WAH_8")

def test_wah_16_small():
    t0 = time.time()
    compress_index("./output/bitmaps/animals_small.txt","./output/compressed","WAH",16)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals_small.txt_WAH_16")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./data/data/compressed/animals_small_WAH_16", "./output/compressed/animals_small.txt_WAH_16")

def test_wah_32_small():
    t0 = time.time()
    compress_index("./output/bitmaps/animals_small.txt","./output/compressed","WAH",32)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals_small.txt_WAH_32")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./data/data/compressed/animals_small_WAH_32", "./output/compressed/animals_small.txt_WAH_32")

def test_wah_64_small():
    t0 = time.time()
    compress_index("./output/bitmaps/animals_small.txt","./output/compressed","WAH",64)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals_small.txt_WAH_64")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./data/data/compressed/animals_small_WAH_64", "./output/compressed/animals_small.txt_WAH_64")

#=========================================================================================
#                                       WAH (animals)
#========================================================================================= 
def test_wah_4():
    t0 = time.time()
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",4)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals.txt_WAH_4")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./mine/mine/compressed/animals_WAH_4", "./output/compressed/animals.txt_WAH_4")    

def test_wah_8():
    t0 = time.time()
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",8)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals.txt_WAH_8")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./mine/mine/compressed/animals_WAH_8", "./output/compressed/animals.txt_WAH_8")

def test_wah_16():
    t0 = time.time()
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",16)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals.txt_WAH_16")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./mine/mine/compressed/animals_WAH_16", "./output/compressed/animals.txt_WAH_16")

def test_wah_32():
    t0 = time.time()
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",32)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals.txt_WAH_32")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./mine/mine/compressed/animals_WAH_32", "./output/compressed/animals.txt_WAH_32")

def test_wah_64():
    t0 = time.time()
    compress_index("./output/bitmaps/animals.txt","./output/compressed","WAH",64)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals.txt_WAH_64")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./mine/mine/compressed/animals_WAH_64", "./output/compressed/animals.txt_WAH_64")

#=========================================================================================
#                                    WAH (animals sorted)
#========================================================================================= 
def test_wah_4_sorted():
    t0 = time.time()
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",4)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals_sorted.txt_sorted_WAH_4")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./mine/mine/compressed/animalsSorted_sorted_WAH_4", "./output/compressed/animals_sorted.txt_sorted_WAH_4")

def test_wah_8_sorted():
    t0 = time.time()
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",8)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals_sorted.txt_sorted_WAH_8")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./mine/mine/compressed/animalsSorted_sorted_WAH_8", "./output/compressed/animals_sorted.txt_sorted_WAH_8")

def test_wah_16_sorted():
    t0 = time.time()
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",16)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals_sorted.txt_sorted_WAH_16")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./mine/mine/compressed/animalsSorted_sorted_WAH_16", "./output/compressed/animals_sorted.txt_sorted_WAH_16")

def test_wah_32_sorted():
    t0 = time.time()
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",32)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals_sorted.txt_sorted_WAH_32")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
    assert cmp_files("./mine/mine/compressed/animalsSorted_sorted_WAH_32", "./output/compressed/animals_sorted.txt_sorted_WAH_32")

def test_wah_64_sorted():
    t0 = time.time()
    compress_index("./output/bitmaps/animals_sorted.txt_sorted","./output/compressed","WAH",64)
    t1 = time.time()
    frame = inspect.stack()[1]
    fs = os.stat("./output/compressed/animals_sorted.txt_sorted_WAH_64")
    print(frame[4][0].strip() + ", time elapsed: " + str(round(t1-t0, 4)) + ", file size: " + str(fs.st_size))
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