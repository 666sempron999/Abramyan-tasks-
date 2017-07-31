'''
While17. Дано целое число N (> 0). Используя операции деления нацело и
взятия остатка от деления, вывести все его цифры, начиная с самой правой
(разряда единиц).
'''

import math as m

N = float(input("N = "))

while N < 0:
	N = float(input("N = "))

a = 0
b = 0

while N > 0:

	a,b = divmod(N,10)
	print(int(b))
	N = a
