"""
Boolean2. Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
"""

A = int(input("Введите число: "))
flag = True

if A % 2 == 0 :
	pass
else:
	flag = False

print(flag)