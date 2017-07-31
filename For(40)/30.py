'''
For30. Дано целое число N (> 1) и две вещественные точки на числовой оси:
A, B (A < B). Отрезок [A, B] разбит на N равных отрезков. Вывести H —
длину каждого отрезка, а также значения функции F(X ) = 1 − sin(X ) в
точках, разбивающих отрезок [A, B]:
F(A), F(A + H), F(A + 2·H), . . . , F(B).
'''

import math as m

N = int(input("Введите N "))

while N <= 1:
	N = int(input("Введите N "))

A = int(input("Введите A "))
B = int(input("Введите B "))

while A > B:
	A = int(input("Введите A "))
	B = int(input("Введите B "))

HCount,ost = divmod(B - A, N)

for i in range(1,HCount + 1):
	print(i,'-', '[A]=',A, '[H]=', A+N)
	print('sin - ',1 - m.sin(A))
	A = A+N

print('Последний отрезок')
print('sin - ',1 - m.sin(B))
print(HCount + 1,'-', '[A]=',A, '[H]=', B)

