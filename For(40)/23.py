'''
For23. Дано вещественное число X и целое число N (> 0). Найти значение
выражения
X − X 3 /(3!) + X 5 /(5!) − . . . + (−1) N ·X 2·N +1 /((2·N+1)!)
(N! = 1·2·. . .·N). Полученное число является приближенным значением
функции sin в точке X.
'''
X = float(input("Введите X "))
N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summ = X

for i in range(1,N+1,2):
	chislitel = pow(-1,i) * pow(X,(2 * i + 1))

	mul = 1.

	for j in range(1,2*N+1):
		mul *= i

	znamenatel = mul

	summ += (chislitel / znamenatel)


print('=')
print(summ)
	