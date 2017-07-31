'''
Boolean15 ◦ . Даны три целых числа: A, B, C. Проверить истинность высказы-
вания: «Ровно два из чисел A, B, C являются положительными».
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

flag = True

if (A > 0 and B > 0 and C < 0
	or
	A < 0 and B > 0 and C > 0
	or
	A > 0 and B < 0 and C > 0
	):
	pass
else:
	flag = False

print(flag)