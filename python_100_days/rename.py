from os import listdir, rename
from os.path import isfile, join

mypath = './'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    print(f)
    if f[0] == 'd':
        rename(f, f[1:])
        # break

    if f[2] not in ('.', '_'):
        print(f)
