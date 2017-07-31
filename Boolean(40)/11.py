'''
Boolean11 ◦ . Даны два целых числа: A, B. Проверить истинность высказыва-
ния: «Числа A и B имеют одинаковую четность».
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))

flag = True

if A % 2 == B % 2:
	pass
else:
	flag = False

print(flag)