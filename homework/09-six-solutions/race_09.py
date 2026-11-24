"""Задание 9. Гонка шести решений. Запуск из корня репозитория:

    python lesson_09/race_09.py

Все решения получают один и тот же худший вход: n разных пропусков, повторов
нет, поэтому каждое решение доходит до конца списка. n не меняется, меняется
только k. Запускайте после того, как заполнили таблицу сложности в отчёте.
"""

import random
from statistics import median
from time import perf_counter

from solutions_09 import SOLUTIONS

N = 5_000
KS = [10, 100, 1_000, 5_000]


def measure_time(func, *args, repeats=3):
    times = []
    for _ in range(repeats):
        start = perf_counter()
        func(*args)
        times.append(perf_counter() - start)
    return median(times)


def main():
    nums = random.Random(9).sample(range(10 * N), N)
    print(f"n = {N}, повторов нет. Время, секунды:\n")
    print(f"{'решение':<10}" + "".join(f"{'k = ' + str(k):>14}" for k in KS))
    for letter, func in SOLUTIONS.items():
        times = [measure_time(func, nums, k) for k in KS]
        print(f"{letter:<10}" + "".join(f"{t:>14.6f}" for t in times))


if __name__ == "__main__":
    main()
