import os
import shutil

def file_name(file_dir):
    result = []
    for root, dirs, files, in os.walk(file_dir):
        for filename in files:
            result.append("./JPEGImages/" + os.path.splitext(filename)[0] + ".jpg")
    return result
def file_namenew(file_dir):
    for root, dirs, files, in os.walk(file_dir):
        print(root)
        print(files)
    return files
if __name__ == '__main__':
    jpegFileNameArr = file_namenew("./SegmentationClass")
