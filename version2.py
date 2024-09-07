import shutil
import os 

dir = '/Users/sangwooklee/Desktop/photography/photo/DIGITAL/RICOH/9월/beagle_party/'
files = os.listdir(dir)

# ===== Make Dir ===== #

jpg = dir + "/JPG"
dng = dir + "/DNG"

try : 
    os.mkdir(jpg)
    os.mkdir(dng)
except FileExistsError:
    pass

# ===== Move Files ===== #

jpg_files = [file for file in files if file.find('.JPG') != -1]
dng_files = [file for file in files if file.find('.DNG') != -1]

for file in jpg_files:
    new_path = dir + 'JPG/' + file
    shutil.move(dir+file, new_path)

for file in dng_files:
    new_path = dir + 'DNG/' + file
    shutil.move(dir+file, new_path)    