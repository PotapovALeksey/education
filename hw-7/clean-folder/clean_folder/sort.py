from .normalize import normalize, clear_archive_name
from pathlib import Path
import re
from .report import *
from .regexp import *
import shutil

ARCHIVES_DIRECTORY_NAME = 'archives'
IMAGES_DIRECTORY_NAME = 'images'
VIDEO_DIRECTORY_NAME = 'video'
DOCUMENTS_DIRECTORY_NAME = 'documents'
AUDIO_DIRECTORY_NAME = 'audio'

SYSTEM_DIRECTORY_NAMES = (ARCHIVES_DIRECTORY_NAME, IMAGES_DIRECTORY_NAME, VIDEO_DIRECTORY_NAME, DOCUMENTS_DIRECTORY_NAME, AUDIO_DIRECTORY_NAME)

def is_matched(regexp, file_name):
    result = re.search(regexp, file_name)

    return bool(result)
def get_directory_name(file_name):
    if is_matched(IMAGE_REGEXP, file_name):
        return IMAGES_DIRECTORY_NAME

    if is_matched(VIDEO_REGEXP, file_name):
        return VIDEO_DIRECTORY_NAME

    if is_matched(DOCUMENT_REGEXP, file_name):
        return DOCUMENTS_DIRECTORY_NAME

    if is_matched(AUDIO_REGEXP, file_name):
        return AUDIO_DIRECTORY_NAME

    if is_matched(ARCHIVE_REGEXP, file_name):
        return ARCHIVES_DIRECTORY_NAME

    return ''

def sort(path: Path):
    for item in path.iterdir():
        if item.is_dir():

            if item.name in SYSTEM_DIRECTORY_NAMES:
                continue

            if len(list(item.iterdir())) == 0:
                item.rmdir()
                add_report_operation('Removed')
            else:
                sort(item)

            continue

        category_directory_name = get_directory_name(item.name)
        category_directory_path = path / category_directory_name
        normalized_name = normalize(item.name)

        if normalized_name != item.name:
            add_report_operation('Renamed')

        if not category_directory_path.exists():
            category_directory_path.mkdir()


        if category_directory_name == ARCHIVES_DIRECTORY_NAME:
            unpack_archive_path = category_directory_path / clear_archive_name(normalized_name)
            shutil.unpack_archive(item.absolute(), unpack_archive_path)
            add_report_operation('Upack archive')


        item.rename(category_directory_path / normalized_name)
        add_report_operation('Moved')


