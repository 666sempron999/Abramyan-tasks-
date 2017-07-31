'''
While30. Даны положительные числа A, B, C. На прямоугольнике разме-
ра A × B размещено максимально возможное количество квадратов со
стороной C (без наложений). Найти количество квадратов, размещенных
на прямоугольнике. Операции умножения и деления не использовать.
'''

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

while A < C or B < C:
	A = float(input("A = "))
	B = float(input("B = "))

buf = B

cnt = 0

while A > C:
	while B > C:
		cnt += 1
		B = B - C

	A = A - C
	cnt += 1
	B = buf

print(cnt)