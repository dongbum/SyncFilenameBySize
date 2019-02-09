#-*- coding: utf-8 -*-

"""
* Written by dongbum ( dongbum9@gmail.com )
* https://github.com/dongbum/SyncFilenameBySize

* 파일 용량을 이용하여 동기화하는 프로그램
* 사용방법 : python syncfilename.py 대상디렉토리 목표디렉토리

* 대상디렉토리에 있는 파일들의 크기을 이용하여 목표디렉토리의 파일명을 변경합니다.
* 파일크기는 바이트 단위로 계산합니다.
* 대상디렉토리에 같은 크기의 파일이 있다면 실행이 중지되고 에러가 출력됩니다.
* 작업은 취소할 수 없습니다.
"""

import sys
import glob
import os
import time
from os.path import *

start_time = time.time()

if len(sys.argv) < 3:
    print("Usage : python syncfilename.py BASE_DIR TARGET_DIR")
    exit(0)

target_dir = sys.argv[2]
target_dict = dict()

for filename in glob.glob(os.path.join(abspath(sys.argv[2]), '*')):
    if (None != target_dict.get(getsize(filename))):
        print("Same file size in base directory detected.")
        exit(0)

    target_dict[getsize(filename)] = filename

for filename in glob.glob(os.path.join(abspath(sys.argv[1]), '*')):
    os.rename(target_dict.get(getsize(filename)), os.path.join(target_dir, basename(filename)))
    print(filename + " -> " + os.path.join(target_dir, basename(filename)))

print("Rename complete. (%.02f seconds)" % (time.time() - start_time))
