'''
If5. Даны три целых числа. Найти количество положительных и количество
отрицательных чисел в исходном наборе.
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

positive = 0
negative = 0

if A > 0:
	positive += 1
else:
	negative += 1

if B > 0:
	positive += 1
else:
	negative += 1

if C > 0:
	positive += 1
else:
	negative += 1

print('positive - ',positive)
print('positive - ',negative)
