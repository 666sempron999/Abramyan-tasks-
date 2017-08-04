"""
Series29. Даны целые числа K, N, а также K наборов целых чисел по N элементов в каждом наборе. Вывести общую сумму всех элементов, входящих в
данные наборы.
"""

import random

resultList = list()
summLoc = 0 
summ = 0

N = int(input("Введите число элементов - "))

while N < 1:
	N = int(input("Введите число элементов - "))

K = int(input("Введите количество наборов - "))

for i in range(1,K+1):

	for x in range(0,N):

		param = random.randint(0, 10)
		resultList.append(param)
		summLoc += param

	print(resultList)
	summ += summLoc
	summLoc = 0
	resultList.clear()

print(summ)



