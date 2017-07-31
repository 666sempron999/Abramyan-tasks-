'''
Boolean16 ◦ . Дано целое положительное число. Проверить истинность выска-
зывания: «Данное число является четным двузначным»..
'''

A = int(input("Введите A: "))

flag = True

while A < 0:
	A = int(input("Введите A: "))

if (A > 9 and A < 100) and A % 2 == 0:
	pass
else:
	flag = False

print(flag)