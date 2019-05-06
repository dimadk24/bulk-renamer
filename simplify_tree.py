import os
import shutil

from utils import get_dirs_recursively, script_dir, get_number_of_files, get_list_of_files, \
    get_parent_dir

directories = get_dirs_recursively(script_dir)

for directory in directories:
    if '__pycache__' in directory:
        continue
    if get_number_of_files(directory) == 1:
        file = get_list_of_files(directory)[0]
        parent_dir = get_parent_dir(directory)
        shutil.move(file, os.path.join(parent_dir))
        os.rmdir(directory)

