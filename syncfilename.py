import sys
import glob
from os.path import *

if len(sys.argv) < 2:
    print("Usage : BASE TARGET")
    exit(0)

print("옵션1 : " + sys.argv[0])
print("옵션2 : " + sys.argv[1])
print("옵션3 : " + sys.argv[2])

for filename in glob.glob(abspath(sys.argv[1]) + '\\*'):
    print(filename + " - " + str(getsize(filename)))

target_dict = dict()

for filename in glob.glob(abspath(sys.argv[2] + '\\*')):
    print(filename + " - " + str(getsize(filename)))
    target_dict.get(getsize(filename))
    target_dict.update(getsize(filename), filename)

