import os
import shutil

WORD = 'АРТДИЗАЙН-'

script_path = os.path.dirname(os.path.abspath(__file__))


def get_list_of_files(dir_name: str) -> list:
    files_in_current_directory: list = os.listdir(dir_name)
    all_files = []
    for file in files_in_current_directory:
        full_path = os.path.join(dir_name, file)
        if os.path.isdir(full_path):
            all_files += get_list_of_files(full_path)
        else:
            all_files.append(full_path)
    return all_files


def remove_part_of_string(word: str, string: str) -> str:
    return string.replace(word, '')


def dir_is_empty(dirname: str) -> bool:
    dir_contents = os.listdir(dirname)
    return len(dir_contents) == 0


if __name__ == '__main__':
    filenames = get_list_of_files(script_path)
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
