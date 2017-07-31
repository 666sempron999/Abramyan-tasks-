'''
If4 . Даны три целых числа. Найти количество положительных чисел в исход-
ном наборе.
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

count = 0

if A > 0:
	count += 1

if B > 0:
	count += 1

if C > 0:
	count += 1

print('positive - 'count)
