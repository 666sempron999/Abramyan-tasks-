'''
For28. Дано вещественное число X (|X | < 1) и целое число N (> 0). Найти
значение выражения
1 + X /2 − 1·X 2 /(2·4) + 1·3·X 3 /(2·4·6) − . . . +
+ (−1) N −1 ·1·3·. . .·(2·N−3)·X N /(2·4·. . .·(2·N)).
'''
X = float(input("Введите X "))

while abs(X) > 1:
	X = float(input("Введите X "))

N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

summ = X

for i in range(1,N+1):

'''Бред какойто'''
	
print('=')
print(summ)
	

