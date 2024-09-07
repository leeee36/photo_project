import shutil
import os 

dir = '/Users/sangwooklee/Desktop/photography/photo/DIGITAL/RICOH/9월/test/' # 폴더 경로
files = os.listdir(dir)

# ===== Make Dir ===== #

jpg = dir + "JPG"   # 파일명1 설정
dng = dir + "DNG"   # 파일명2 설정

try : 
    os.mkdir(jpg)
    os.mkdir(dng)
except FileExistsError :
    pass

# ===== Move Files ===== #

jpg_files = [file for file in files if file.find('.JPG') != -1]
dng_files = [file for file in files if file.find('.DNG') != -1]

for file in jpg_files:
    new_path = jpg + '/' + file
    shutil.move(dir+file, new_path)

for file in dng_files:
    new_path = dng + '/' + file
    shutil.move(dir+file, new_path)