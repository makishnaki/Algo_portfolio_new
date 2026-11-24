"""Задание 7, часть 3. Имя объекта Git для содержимого файла.

Запуск из корня репозитория:

    python lesson_07/git_hash_07.py README.md

Программа печатает тот же хеш, что и `git hash-object --no-filters README.md`.
"""

import hashlib
import sys


def blob_hash(data: bytes) -> str:
    """Вернуть имя blob-объекта Git для содержимого data.

    Git дописывает перед содержимым заголовок: слово blob, пробел, размер
    содержимого в байтах и нулевой байт. От заголовка вместе с содержимым
    считается SHA-1, ответ — 40 шестнадцатеричных символов.

    >>> blob_hash(b"test content\\n")
    'd670460b4b4aece5915caf5c68d12f560a9fe3e4'

    Подсказка: hashlib.sha1(байты).hexdigest().
    """
    raise NotImplementedError


if __name__ == "__main__":
    with open(sys.argv[1], "rb") as file:
        print(blob_hash(file.read()))
