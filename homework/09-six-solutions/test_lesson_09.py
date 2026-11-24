"""Тесты задания 9. Запуск из корня репозитория:

    pytest lesson_09 -q

Тесты проверяют ваши контрпримеры из counterexamples_09.py: решение
с ошибкой на них должно ответить не так, как правильный перебор ниже.
"""

from counterexamples_09 import BUGGY
from solutions_09 import SOLUTIONS


def expected(nums, k):
    """Правильный ответ полным перебором всех пар."""
    return any(
        nums[i] == nums[j]
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
        if j - i <= k
    )


def test_two_buggy_solutions_named():
    assert len(BUGGY) == 2, "запишите контрпримеры ровно для двух решений"
    assert set(BUGGY) <= set(SOLUTIONS), "ключи — буквы решений: 'a', 'b', ..."


def test_counterexamples_have_right_shape():
    for letter, case in BUGGY.items():
        nums, k = case
        assert isinstance(nums, list) and all(isinstance(x, int) for x in nums), letter
        assert isinstance(k, int) and k >= 0, letter


def test_counterexamples_are_short():
    for letter, (nums, _) in BUGGY.items():
        assert len(nums) <= 10, f"{letter}: вход длиннее 10 чисел"


def test_counterexamples_break_solutions():
    assert BUGGY, "словарь BUGGY пуст"
    for letter, (nums, k) in BUGGY.items():
        got = SOLUTIONS[letter](list(nums), k)
        assert got != expected(nums, k), (
            f"решение {letter} на {nums}, k={k} отвечает {got} — и это верно"
        )
