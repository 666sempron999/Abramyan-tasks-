'''
If12 ◦ . Даны три числа. Найти наименьшее из них.
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

minimal = 0

if A < B and A < C:
	minimal = A

if B < A and B < C:
	minimal = B

if C < A and C < B:
	minimal = C

print('minimal - ',minimal)