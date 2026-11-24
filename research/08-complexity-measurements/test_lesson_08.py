"""Тесты задания 8. Запуск из корня репозитория:

    pytest lesson_08 -q
"""

from algorithms_08 import (
    merge_intervals,
    unique_in_order_list,
    unique_in_order_set,
    window_sum_shift,
    window_sum_slices,
)
from measure_08 import growth_ratios, make_numbers, measure_k_series, measure_time


# ---------- make_numbers ----------

def test_numbers_length_and_range():
    nums = make_numbers(1_000)
    assert len(nums) == 1_000
    assert all(0 <= x < 10_000 for x in nums)


def test_numbers_are_distinct():
    nums = make_numbers(5_000)
    assert len(set(nums)) == len(nums)


def test_numbers_repeat_with_same_seed():
    assert make_numbers(300, seed=1) == make_numbers(300, seed=1)
    assert make_numbers(300, seed=1) != make_numbers(300, seed=2)


# ---------- measure_time ----------

def test_measure_time_calls_func_repeats_times():
    calls = []
    measure_time(calls.append, "x", repeats=4)
    assert calls == ["x"] * 4


def test_measure_time_returns_positive_seconds():
    seconds = measure_time(sum, list(range(10_000)))
    assert isinstance(seconds, float)
    assert 0 < seconds < 1


# ---------- growth_ratios ----------

def test_ratios_example():
    assert growth_ratios([1.0, 2.0, 8.0]) == [2.0, 4.0]


def test_ratios_short_lists():
    assert growth_ratios([]) == []
    assert growth_ratios([0.5]) == []


# ---------- measure_k_series ----------

def test_k_series_keeps_order_of_k():
    result = measure_k_series(200, [1, 100, 50, 200])
    assert [k for k, _ in result] == [1, 100, 50, 200]
    assert all(seconds > 0 for _, seconds in result)


# ---------- сами функции (уже работают) ----------

def test_windows_agree():
    nums = make_numbers(500)
    for k in (1, 7, 250, 500):
        assert window_sum_slices(nums, k) == window_sum_shift(nums, k)


def test_merge_example():
    assert merge_intervals([[8, 10], [1, 3], [2, 6], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_merge_touching():
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]


def test_unique_agree():
    items = [3, 1, 3, 2, 1, 5]
    assert unique_in_order_list(items) == unique_in_order_set(items) == [3, 1, 2, 5]
