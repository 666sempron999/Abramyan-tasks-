"""
Boolean5–. Даны два целых числа: A, B. Проверить истинность высказывания:
«Справедливы неравенства A ‚ 0 или B < -2.
"""

A = int(input("Введите число A: "))

B = int(input("Введите число B: "))
flag = True

if A >= 0 or B < -2:
	pass
else:
	flag = False

print(flag)