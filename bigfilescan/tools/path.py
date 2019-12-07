import glob
import os
from typing import AnyStr
from .dt import timestamp_to_str


def get_type(fullpath: AnyStr) -> AnyStr or None:
    directory = 'Directory' if os.path.isdir(fullpath) else None
    file = 'File' if os.path.isfile(fullpath) else None
    return directory or file


def scan_dir(path):
    files = glob.glob(path + '**', recursive=True)
    file_list = list()
    for file in files:
        file_size = os.path.getsize(file)
        file_create_datetime = timestamp_to_str(os.path.getctime(file))
        type_ = get_type(file)
        file_list.append((file, file_size, file_create_datetime, type_))
    sorted(file_list, reverse=True)
    return file_list
