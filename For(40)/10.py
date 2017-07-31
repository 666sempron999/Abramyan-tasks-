'''
For10. Дано целое число N (> 0). Найти сумму
1 + 1/2 + 1/3 + . . . + 1/N
(вещественное число).
'''
import math as m


N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summa = 1
coef = 1

for i in range(1,N):
	summa += coef/(i+1)

print(summa)