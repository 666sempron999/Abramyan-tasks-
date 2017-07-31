'''
If15. Даны три числа. Найти сумму двух наибольших из них.
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

sumMax = 0

if A < B < C:
	sumMax = B + C

elif B < C < A:
	sumMax = C + A

elif C < A < B:
	sumMax = A + B

else:
	sumMax = max(A, B, C)


print('sumMax = ',sumMax)
