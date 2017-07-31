'''
For27. Дано вещественное число X (|X | < 1) и целое число N (> 0). Найти
значение выражения
X + 1·X 3 /(2·3) + 1·3·X 5 /(2·4·5) + . . . +
+ 1·3·. . .·(2·N−1)·X 2·N +1 /(2·4·. . .·(2·N)·(2·N+1)).
Полученное число является приближенным значением функции arcsin в
точке X.
'''
X = float(input("Введите X "))

while abs(X) > 1:
	X = float(input("Введите X "))

N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summ = X

for i in range(1,N+1):
	chislitel = (2 * i - 1) * pow(X, (2*i+1))
	znamenatel = (2 * i)  * (2 * i + 1)
	summ += chislitel / znamenatel
	
print('=')
print(summ)
	

