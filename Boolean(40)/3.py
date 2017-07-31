"""
Boolean3–. Дано целое число A. Проверить истинность высказывания: «Чис
ло A является четным».
"""

A = int(input("Введите число: "))
flag = True

if A % 2 == 0 :
	pass
else:
	flag = False

print(flag)