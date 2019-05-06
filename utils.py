import os
from glob import glob

script_dir = os.path.dirname(os.path.abspath(__file__))


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


def get_dirs_recursively(dirname: str) -> list:
    return glob(os.path.join(dirname, '**/'), recursive=True)


def get_number_of_files(dirname: str) -> int:
    files = [
        name for name in os.listdir(dirname)
        if os.path.isfile(os.path.join(dirname, name))
    ]
    return len(files)


def get_parent_dir(dirname: str) -> str:
    return os.path.join(dirname, os.pardir)
