"""
Boolean8–. Даны два целых числа: A, B. Проверить истинность высказывания:
«Каждое из чисел A и B нечетное».
"""

A = int(input("Введите число A: "))

B = int(input("Введите число B: "))

flag = True

if A % 2 == 0 and B % 2 == 0:
	pass
else:
	flag = False

print(flag)