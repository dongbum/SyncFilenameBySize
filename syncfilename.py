import sys
import glob
import os
from os.path import *

if len(sys.argv) < 2:
    print("Usage : python syncfilename.py BASE_DIR TARGET_DIR")
    exit(0)

target_dir = sys.argv[2]
target_dict = dict()

# 타겟의 파일들을 크기와 파일명으로 구분하여 입력
for filename in glob.glob(abspath(sys.argv[2] + '\\*')):
    # print(filename + " - " + str(getsize(filename)))
    if (None != target_dict.get(getsize(filename))):
        print("Same file size detected.")
        exit(0)

    target_dict[getsize(filename)] = filename

# 대상의 파일들을 검색
for filename in glob.glob(abspath(sys.argv[1]) + '\\*'):
    os.rename(target_dict.get(getsize(filename)), target_dir + '\\' + basename(filename))


