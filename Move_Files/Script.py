#https://codereview.stackexchange.com/questions/138852/move-files-to-specific-directory-according-to-file-extension
import os
import shutil

fullpath = os.path.join
start_directory = "C:\\Users\\gcfil\\OneDrive - Universidad de los Andes\\Libros\\AWZ3_MOBI\\"
target_directory = "C:\\Users\\gcfil\\Desktop\\Move_files\\AWZ3"

for root, dirs, files in os.walk(start_directory):
    for name in files:
        source = fullpath(root, name)
        if name.endswith('azw3'):
            shutil.copy(source,fullpath(target_directory, name))