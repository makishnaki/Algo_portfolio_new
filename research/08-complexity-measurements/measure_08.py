"""Задание 8. Замеры пяти функций на разных объёмах данных.

Запуск из корня репозитория:

    python lesson_08/measure_08.py

Программа печатает таблицу и сохраняет замеры в два файла рядом с собой:
results_08.csv (время от n) и results_08_k.csv (время от k при постоянном n).
Графики по этим файлам строит plot_08.py.

Напишите тела четырёх функций с пометкой TODO. Остальное уже готово.
"""

import csv
import random
from pathlib import Path
from statistics import median
from time import perf_counter

from algorithms_08 import (
    merge_intervals,
    unique_in_order_list,
    unique_in_order_set,
    window_sum_shift,
    window_sum_slices,
)

HERE = Path(__file__).parent
SIZES = [1_000, 2_000, 4_000, 8_000, 16_000]
K_SERIES_N = 10_000
K_SERIES = [1, 1_000, 2_500, 5_000, 7_500, 9_000, 10_000]


def make_numbers(n, seed=8):
    """Вернуть список из n разных целых чисел в случайном порядке.

    Числа берутся из диапазона от 0 до 10·n. При одном и том же seed
    список всегда одинаковый, поэтому замер можно повторить.

    Подсказка: random.Random(seed) — свой генератор, у него есть метод sample.
    """
    # TODO
    raise NotImplementedError


def make_intervals(n, seed=8):
    """Вернуть n интервалов [начало, конец]; конец больше начала на 0–5."""
    rng = random.Random(seed)
    intervals = []
    for _ in range(n):
        start = rng.randrange(10 * n)
        intervals.append([start, start + rng.randint(0, 5)])
    return intervals


def measure_time(func, *args, repeats=5):
    """Вызвать func(*args) repeats раз и вернуть медиану времени в секундах.

    Так же, как в программе measurements.py с занятия 4: perf_counter до
    и после вызова, время каждого вызова в список, в ответ — медиана.
    """
    # TODO
    raise NotImplementedError


def growth_ratios(times):
    """Во сколько раз выросло время при каждом удвоении n.

    growth_ratios([1.0, 2.0, 8.0]) == [2.0, 4.0]
    Для пустого списка и списка из одного времени ответ — пустой список.
    """
    # TODO
    raise NotImplementedError


def measure_k_series(n, ks, repeats=3):
    """Время window_sum_slices на одних и тех же n числах при разных k.

    Вернуть список пар (k, секунды) в том же порядке, что ks.
    Данные готовятся один раз, до замеров: make_numbers(n).
    """
    # TODO
    raise NotImplementedError


# Что измеряем: имя в таблице, функция, как построить вход размера n,
# сколько раз повторить замер. Быстрые функции повторяем чаще: их время —
# доли миллисекунды, и одиночный замер сильно скачет.
EXPERIMENTS = [
    ("window_sum_slices", window_sum_slices, lambda n: (make_numbers(n), n // 2), 3),
    ("window_sum_shift", window_sum_shift, lambda n: (make_numbers(n), n // 2), 15),
    ("merge_intervals", merge_intervals, lambda n: (make_intervals(n),), 15),
    ("unique_in_order_list", unique_in_order_list, lambda n: (make_numbers(n),), 3),
    ("unique_in_order_set", unique_in_order_set, lambda n: (make_numbers(n),), 15),
]


def main():
    rows = []
    print(f"{'функция':<22}" + "".join(f"{n:>12}" for n in SIZES))
    for name, func, make_args, repeats in EXPERIMENTS:
        times = []
        for n in SIZES:
            args = make_args(n)
            seconds = measure_time(func, *args, repeats=repeats)
            times.append(seconds)
            rows.append((name, n, seconds))
        print(f"{name:<22}" + "".join(f"{t:>12.6f}" for t in times))
        print(f"{'  рост при удвоении':<22}{'':>12}" + "".join(f"{r:>12.2f}" for r in growth_ratios(times)))

    with open(HERE / "results_08.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["function", "n", "seconds"])
        writer.writerows(rows)

    print(f"\nwindow_sum_slices при n = {K_SERIES_N}:")
    k_rows = measure_k_series(K_SERIES_N, K_SERIES)
    for k, seconds in k_rows:
        print(f"  k = {k:>6}: {seconds:.6f} с")

    with open(HERE / "results_08_k.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["k", "seconds"])
        writer.writerows(k_rows)


if __name__ == "__main__":
    main()
