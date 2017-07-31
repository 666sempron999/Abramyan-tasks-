'''
For29. Дано целое число N (> 1) и две вещественные точки на числовой оси:
A, B (A < B). Отрезок [A, B] разбит на N равных отрезков. Вывести H —
длину каждого отрезка, а также набор точек
A, A + H, A + 2·H, A + 3·H, . . . , B,
образующий разбиение отрезка [A, B].
'''
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
	A = A+N

print('Последний отрезок')
print(HCount + 1,'-', '[A]=',A, '[H]=', B)

