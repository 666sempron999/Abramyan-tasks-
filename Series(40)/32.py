"""
Series32. Даны целые числа K, N, а также K наборов целых чисел по N элементов в каждом наборе. Для каждого набора вывести номер его первого
элемента, равного 2, или число 0, если в данном наборе нет двоек.
"""

import random

resultList = list()

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
		print("Она расположена на ",resultList.index(2)+1,"позиции")
	else:
		print(0)

	resultList.clear()
