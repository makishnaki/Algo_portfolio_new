"""Задание 8. Пять функций, которые мы измеряем. Этот файл не меняйте.

Какая у каждой функции сложность, вы выясняете замером, а потом сверяете
с кодом.
"""


def window_sum_slices(nums, k):
    """Наибольшая сумма отрезка длины k: каждое окно складывается заново срезом."""
    best = sum(nums[:k])
    for i in range(1, len(nums) - k + 1):
        best = max(best, sum(nums[i:i + k]))
    return best


def window_sum_shift(nums, k):
    """Наибольшая сумма отрезка длины k: окно сдвигается (модуль 9)."""
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best


def merge_intervals(intervals):
    """Объединение пересекающихся интервалов (модуль 12)."""
    result = []
    for start, end in sorted(intervals):
        if result and start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result


def unique_in_order_list(items):
    """Элементы без повторов в порядке первого появления."""
    result = []
    for x in items:
        if x not in result:
            result.append(x)
    return result


def unique_in_order_set(items):
    """Элементы без повторов в порядке первого появления (модуль 19)."""
    seen = set()
    result = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
