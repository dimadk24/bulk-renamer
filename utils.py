import os


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

