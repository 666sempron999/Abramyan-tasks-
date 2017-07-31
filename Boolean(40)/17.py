'''
Boolean17 ◦ . Дано целое положительное число. Проверить истинность выска-
зывания: «Данное число является нечетным трехзначным».
'''

A = int(input("Введите A: "))

flag = True

while A < 0:
	A = int(input("Введите A: "))

if (A > 99 and A < 1000) and A % 2 != 0:
	pass
else:
	flag = False

print(flag)