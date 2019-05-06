import os
import shutil

from utils import get_list_of_files, remove_part_of_string, dir_is_empty, script_dir

WORD = 'АРТДИЗАЙН-'

if __name__ == '__main__':
    filenames = get_list_of_files(script_dir)
    for filename in filenames:
        if WORD in filename:
            directory = os.path.dirname(filename)
            new_filename = remove_part_of_string(WORD, filename)
            print(filename, new_filename)
            new_directory = os.path.dirname(new_filename)
            os.makedirs(new_directory, exist_ok=True)
            shutil.move(filename, new_filename)
            if dir_is_empty(directory):
                os.rmdir(directory)
