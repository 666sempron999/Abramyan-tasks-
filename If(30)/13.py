'''
If13. Даны три числа. Найти среднее из них (то есть число, расположенное
между наименьшим и наибольшим).
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

average = 0

if A < B < C:
	average = B

if B < C < A:
	average = C

if C < A < B:
	average = A

print('average - ',average)