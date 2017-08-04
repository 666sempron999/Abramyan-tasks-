"""
Series33. Даны целые числа K, N, а также K наборов целых чисел по N элементов в каждом наборе. Для каждого набора вывести номер его последнего
элемента, равного 2, или число 0, если в данном наборе нет двоек.
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
		resultList.reverse()
		pos = resultList.index(2)
		pos = len(resultList) - pos

		print("Позиция последнего вхождения двойки",pos)
	else:
		print(0)

	print("_______________________________")

	resultList.clear()
