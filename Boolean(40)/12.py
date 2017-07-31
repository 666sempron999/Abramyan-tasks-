'''
Boolean12 ◦ . Даны три целых числа: A, B, C. Проверить истинность высказы-
вания: «Каждое из чисел A, B, C положительное».
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

flag = True

if A and B and C > 0:
	pass
else:
	flag = False

print(flag)