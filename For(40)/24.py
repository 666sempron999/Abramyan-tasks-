'''
For24. Дано вещественное число X и целое число N (> 0). Найти значение
выражения
1 − X 2 /(2!) + X 4 /(4!) − . . . + (−1) N ·X 2·N /((2·N)!)
(N! = 1·2·. . .·N). Полученное число является приближенным значением
функции cos в точке X.
'''
X = float(input("Введите X "))
N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summ = 1

for i in range(1,N):
	chislitel = pow(-1,i) * pow(X,(2 * i))

	mul = 1.

	for j in range(1,2*N):
		mul *= i

	znamenatel = mul

	summ += (chislitel / znamenatel)


print('=')
print(summ)
	