import re
from .regexp import ARCHIVE_REGEXP

symbols = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

dictionary = { ord(a): ord(b) for a, b in zip(*symbols) }

REGEXP = r'[^\w]'

def transliterate(text):
    return text.translate(dictionary)


def clear_name(filename):
    if '.' in filename:
        name, file_format = filename.rsplit('.', 1)

        return '.'.join((re.sub(REGEXP, "", name), file_format))
    else:
        return filename

def normalize(filename):
    return transliterate(clear_name(filename))

def clear_archive_name(archive_name):
    return re.sub(ARCHIVE_REGEXP, '', archive_name)