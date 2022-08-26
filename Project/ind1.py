# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано число m(1<=m<=7). Вывести на экран название дня недели, который соответствует
этому номеру.
"""

import sys


if __name__ == '__main__':
    m = int(input("Введите номер дня в недели: "))

    if m == 1:
        print("Понедельник")
    elif m == 2:
        print("Вторник")
    elif m == 3:
        print("Среда")
    elif m == 4:
        print("Четверг")
    elif m == 5:
        print("Пятница")
    elif m == 6:
        print("Суббота")
    elif m == 7:
        print("Воскресенье")
    else:
        print("Ошибка, такого дня нет!", file=sys.stderr)
        exit(1)