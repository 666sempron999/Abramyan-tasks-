'''
For11. Дано целое число N (> 0). Найти сумму
N 2 + (N + 1) 2 + (N + 2) 2 + . . . + (2·N) 2
(целое число).
'''
import math as m


N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summa = pow(N,2)

for i in range(1,N*2):
	summa += pow((N + 1),2)

print(summa)