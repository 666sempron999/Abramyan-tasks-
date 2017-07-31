"""
Boolean7–. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и C».
"""

A = int(input("Введите число A: "))

B = int(input("Введите число B: "))

C = int(input("Введите число C: "))

flag = True

if A < B < C:
	pass
else:
	flag = False

print(flag)