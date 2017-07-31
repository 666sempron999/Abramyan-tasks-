"""
Begin17 ◦ . Даны три точки A, B, C на числовой оси. Найти длины отрезков AC
и BC и их сумму.
"""
import math as m

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

AC = abs(C - A)
BC = abs(C - B)

print(AC, " " , BC)
