'''
Case12. Элементы окружности пронумерованы следующим образом: 1 — ра-
диус R, 2 — диаметр D = 2·R, 3 — длина L = 2·π·R, 4 — площадь кру-
га S = π·R 2 . Дан номер одного из этих элементов и его значение. Вывести
значения остальных элементов данной окружности (в том же порядке). В
качестве значения π использовать 3.14.
'''

import math as m

print('1 - радиус')
print('2 - диаметр')
print('3 - длинна')
print('4 - площадь')

n = int(input("Введите номер: "))
while n > 4 or n < 1:
	n = int(input("Введите номер: "))

o = float(input("Введите переменную: "))

R = 0
D = 0
L = 0
S = 0

if n == 1:
	R = o
	D = 2 * R
	L = math.pi * D
	S = math.pi * (R*R)

elif n == 2:
	D = o
	R = D / 2
	L = math.pi * D
	S = math.pi * (R*R)

elif n == 3:
	L = o
	R = L / (2 * math.pi)
	D = 2 * R
	S = math.pi * (R*R)

elif n == 4:
	S = o
	R = m.sqrt(S / math.pi)
	D = 2 * R
	L = math.pi * D

print('Радиус ',R)
print('Диаметр ',D)
print('Длинна ',L)
print('Площадь ',S)
