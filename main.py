import shutil
file = "new.py"
file_copy = "new_copy.py"
try:
    shutil.copyfile(file,file_copy)
    shutil.copy2(file, file_copy)
finally:
    print("End")