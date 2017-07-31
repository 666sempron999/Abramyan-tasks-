'''
For22. Дано вещественное число X и целое число N (> 0). Найти значение
выражения
1 + X + X 2 /(2!) + . . . + X N /(N!)
(N! = 1·2·. . .·N). Полученное число является приближенным значением
функции exp в точке X.
'''
X = float(input("Введите X "))
N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

mul = 1.
summ = 0

for i in range(1,N+1):
	mul *= i
	print(1 / mul)
	summ = summ + (1 / mul)

print('=')
print(summ)
	