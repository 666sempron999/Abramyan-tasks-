'''
For17. Дано вещественное число A и целое число N (> 0). Используя один
цикл, найти сумму
1 + A + A 2 + A 3 + . . . + A N .
'''
A = int(input("Введите A "))
N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summ = 0

for i in range(0,N):
	summ = summ	+ pow(A,i)
	print(pow(A,i))
	print('+')

print('Сумма - ',summ)