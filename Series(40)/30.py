"""
Series30–. Даны целые числа K, N, а также K наборов целых чисел по N элементов в каждом наборе. Для каждого набора вывести сумму его элементов.
"""

import random

resultList = list()
summLoc = 0 

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
	print("сумма",i,"ряда",summLoc)

	summLoc = 0
	resultList.clear()





