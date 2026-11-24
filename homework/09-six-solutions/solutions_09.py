"""Задание 9. Шесть решений одной задачи. Этот файл не меняйте.

Задача. Турникет записывает номера пропусков в порядке проходов: nums.
Если один и тот же пропуск прошёл дважды и между этими проходами было
не больше k шагов (номера проходов i и j, i != j, |i − j| <= k), охрана
хочет об этом знать. Вернуть True, если такая пара есть, иначе False.

    near_repeat([7, 3, 7], 2)    -> True    проходы 0 и 2, разница 2
    near_repeat([7, 3, 7], 1)    -> False   разница 2 больше k = 1
    near_repeat([5, 5], 0)       -> False   при k = 0 пар не бывает

Решения прислали шесть разных кандидатов. Две из них иногда отвечают
неверно. Какие — выясните сами.
"""


def near_repeat_a(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, min(i + k + 1, len(nums))):
            if nums[i] == nums[j]:
                return True
    return False


def near_repeat_b(nums, k):
    for i in range(len(nums)):
        if nums[i] in nums[i + 1:i + k + 1]:
            return True
    return False


def near_repeat_c(nums, k):
    last = {}
    for i, x in enumerate(nums):
        if x in last and i - last[x] <= k:
            return True
        last[x] = i
    return False


def near_repeat_d(nums, k):
    window = set()
    for i, x in enumerate(nums):
        if x in window:
            return True
        window.add(x)
        if len(window) > k:
            window.remove(nums[i - k])
    return False


def near_repeat_e(nums, k):
    first = {}
    for i, x in enumerate(nums):
        if x in first and i - first[x] <= k:
            return True
        if x not in first:
            first[x] = i
    return False


def near_repeat_f(nums, k):
    window = set()
    for i, x in enumerate(nums):
        if x in window:
            return True
        window.add(x)
        if i >= k + 1:
            window.remove(nums[i - k - 1])
    return False


SOLUTIONS = {
    "a": near_repeat_a,
    "b": near_repeat_b,
    "c": near_repeat_c,
    "d": near_repeat_d,
    "e": near_repeat_e,
    "f": near_repeat_f,
}
