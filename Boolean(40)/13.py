'''
Boolean13 ◦ . Даны три целых числа: A, B, C. Проверить истинность высказы-
вания: «Хотя бы одно из чисел A, B, C положительное».
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

flag = True

if A > 0 or B > 0 or C > 0:
	pass
else:
	flag = False

print(flag)