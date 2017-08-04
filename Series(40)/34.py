"""
Series34. Даны целые числа K, N, а также K наборов целых чисел по N элементов в каждом наборе. Для каждого набора выполнить следующее действие: если в наборе содержится число 2, то вывести сумму его элементов;
если в наборе нет двоек, то вывести 0.
"""

import random

resultList = list()

N = int(input("Введите число элементов - "))

while N < 1:
	N = int(input("Введите число элементов - "))

K = int(input("Введите количество наборов - "))

print("_______________________________")

for i in range(1,K+1):

	for x in range(0,N):

		param = random.randint(0, 10)
		resultList.append(param)

	print(resultList)
	if 2 in resultList:
		print("В этом наборе есть 2")
		print("Сумма - ",sum(resultList))
	else:
		print(0)

	print("_______________________________")

	resultList.clear()
