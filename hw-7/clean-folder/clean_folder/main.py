import sys
from datetime import datetime
from pathlib import Path
from clean_folder.report import get_report
from clean_folder.sort import sort

class DirectoryNotFound(Exception):
    pass

def clean_folder():
    try:
        dir_name = sys.argv[1]
        path = Path(dir_name)

        if not path.exists():
            raise DirectoryNotFound

        sort(path)

        start_time, report = get_report()

        report_text = f'Start script: {start_time}\n\n{report}\nEnd script: {datetime.now()}'

        log_file_name = f'{start_time}_log.txt'
        with open(path / log_file_name, 'w') as log_file:
            log_file.write(report_text)

        print(f'The folder is cleared successfully.\nYou can check detail information in the file {path / log_file_name}')


    except IndexError:
        print('You didn\'t provide directory name. Please try again providing it!')
    except DirectoryNotFound:
        print('The directory name is incorrect. The directory path may not exist. Please try again!')

if __name__ == '__main__':
    clean_folder()

