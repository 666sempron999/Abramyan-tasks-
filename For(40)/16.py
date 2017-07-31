'''
For16 ◦ . Дано вещественное число A и целое число N (> 0). Используя один
цикл, вывести все целые степени числа A от 1 до N.
'''
A = float(input("Введите A "))
N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

intPart = 0
floatpart = 0
mul = 1

for x in range(1, N + 1):
	mul = mul * A
	intPart = int(mul)
	floatpart = mul
	if intPart == floatpart:
		print(mul)
	else:
		pass
