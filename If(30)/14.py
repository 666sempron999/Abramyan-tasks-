'''
If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из
данных чисел.
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

maximal = 0
minimal = 0

if A < B < C:
	maximal = C
	minimal = A

if B < C < A:
	maximal = A
	minimal = B

if C < A < B:
	maximal = B
	minimal = C

print('maximal - ',maximal)
print('minimal - ',minimal)