import pandas
import os
import shutil

dir = '/Users/sangwooklee/Desktop/photography/photo/DIGITAL/RICOH/9월/beagle_party'
files = os.listdir(dir)

# ===== Make Dir ===== #

jpg = dir + "/JPG"
dng = dir + "/DNG"

try : 
    os.mkdir(jpg)
    os.mkdir(dng)
except FileExistsError:
    pass

# ===== Checking File ===== #

for file in files :
    if os.path.isdir(file) == False :
        name, ext = os.path.splitext(file)
        if ext == ".JPG" :
            shutil.move(name+ext, jpg)
        else :
            shutil.move(name+ext, dng)
