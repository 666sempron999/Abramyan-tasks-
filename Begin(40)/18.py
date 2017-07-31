'''
Begin18 ◦ . Даны три точки A, B, C на числовой оси. Точка C расположена
между точками A и B. Найти произведение длин отрезков AC и BC.
'''
import math as m

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

while C <= A or C >= B:
    print("C must betwin A and B")
    A = int(input("Введите A: "))
    B = int(input("Введите B: "))
    C = int(input("Введите C: "))

AC = abs(C - A)
BC = abs(C - B)

P = AC * BC

print(P)
