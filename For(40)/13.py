'''
For13 ◦ . Дано целое число N (> 0). Найти значение выражения
1.1 − 1.2 + 1.3 − . . .
'''
import math as m


N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summ = 0
coef = 1.1

for i in range(1,N):
	if i % 2 != 0:
		summ = summ + coef
	else:
		summ = summ - coef

	coef += 0.1

	print('[', i , ']',coef)

print(summ)