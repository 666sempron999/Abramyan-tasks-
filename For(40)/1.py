'''
For1. Даны целые числа K и N (N > 0). Вывести N раз число K.
'''

N = int(input("Введите N: "))

K = int(input("Введите K: "))

for i in range(0,N):
	print('[', i + 1, ']',K)