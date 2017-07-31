"""
Boolean4–. Даны два целых числа: A, B. Проверить истинность высказывания:
«Справедливы неравенства A > 2 и B <= 3».
"""

A = int(input("Введите число A: "))

B = int(input("Введите число B: "))
flag = True

if A > 2 and B <= 3:
	pass
else:
	flag = False

print(flag)