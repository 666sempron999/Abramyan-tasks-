"""
Series31. Даны целые числа K, N, а также K наборов целых чисел по N элементов в каждом наборе. Найти количество наборов, содержащих число 2.
Если таких наборов нет, то вывести 0
"""

import random

resultList = list()

counter = 0

N = int(input("Введите число элементов - "))

while N < 1:
	N = int(input("Введите число элементов - "))

K = int(input("Введите количество наборов - "))

for i in range(1,K+1):

	for x in range(0,N):

		param = random.randint(0, 10)
		resultList.append(param)

	print(resultList)
	if 2 in resultList:
		print("В этом наборе есть 2")
		counter += 1
	else:
		print(0)

	resultList.clear()

print("Обнаружено ", counter, " списков с числом 2")





