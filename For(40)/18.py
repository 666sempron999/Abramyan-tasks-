'''
For18. Дано вещественное число A и целое число N (> 0). Используя один
цикл, найти значение выражения
1 − A + A 2 − A 3 + . . . + (−1) N ·A N .
'''
A = float(input("Введите A "))
N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summ = 1 - A

for i in range(1,N+1):
	print(summ)
	summ += pow(-1,i) * pow(A,i)
	
