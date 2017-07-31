'''
For26. Дано вещественное число X (|X | < 1) и целое число N (> 0). Найти
значение выражения
X − X 3 /3 + X 5 /5 − . . . + (−1) N ·X 2·N +1 /(2·N+1).
Полученное число является приближенным значением функции arctg в
точке X.
'''
X = float(input("Введите X "))

while abs(X) > 1:
	X = float(input("Введите X "))

N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summ = X

for i in range(2,N):
	summ += pow(-1, i) * ( pow(X, 2*i+1) / 2 * (i + 1))
	print(summ)

print('=')
print(summ)
	