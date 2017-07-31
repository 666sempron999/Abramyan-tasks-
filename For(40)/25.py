'''
For25. Дано вещественное число X (|X | < 1) и целое число N (> 0). Найти
значение выражения
X − X 2 /2 + X 3 /3 − . . . + (−1) N −1 ·X N /N.
Полученное число является приближенным значением функции ln в точ-
ке 1 + X.
'''
X = float(input("Введите X "))

while abs(X) > 1:
	X = float(input("Введите X "))

N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summ = X

for i in range(2,N+1):
	summ += pow(-1, i-1) * pow(X,i)/i
	print(summ)

print('=')
print(summ)
	