"""Тесты задания 7. Запуск из корня репозитория:

    pytest lesson_07 -q

Ожидаемые хеши получены командой `git hash-object --no-filters`.
"""

from git_hash_07 import blob_hash


def test_example_from_pro_git():
    assert blob_hash(b"test content\n") == "d670460b4b4aece5915caf5c68d12f560a9fe3e4"


def test_empty_file():
    assert blob_hash(b"") == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"


def test_hello():
    assert blob_hash(b"hello\n") == "ce013625030ba8dba906f756967f9e9ca394464a"


def test_windows_line_endings_are_bytes_too():
    assert blob_hash(b"a\r\nb\r\n") == "c30dea8a3641ea99b125d04d599d843712292759"


def test_one_byte_changes_whole_hash():
    first = blob_hash(b"hello\n")
    second = blob_hash(b"Hello\n")
    assert len(first) == len(second) == 40
    same = sum(a == b for a, b in zip(first, second))
    assert same < 20
