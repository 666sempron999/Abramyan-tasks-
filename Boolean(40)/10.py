"""
Boolean10–. Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное».
"""

A = int(input("Введите число A: "))

B = int(input("Введите число B: "))

if (A % 2 != 0 and B % 2 == 0) or (A % 2 == 0 and B % 2 != 0):
	print(True)
else:
	print(False)