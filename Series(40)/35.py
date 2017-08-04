"""
Series35. Дано целое число K, а также K наборов ненулевых целых чисел.
Признаком завершения каждого набора является число 0. Для каждого набора вывести количество его элементов. Вывести также общее количество
элементов во всех наборах
"""

import random

resultList = list()
globalCounter = 0

N = int(input("Введите число элементов (оно равно и числу наборов) - "))

while N < 1:
	N = int(input("Введите число элементов - "))


print("_______________________________")

for i in range(1,N+1):

	for x in range(0,N):

		param = random.randint(0, 10)
		resultList.append(param)
		if param == 0:
			break

	print(resultList)

	print("Длинна списка - ",len(resultList))
	globalCounter += len(resultList)
	print("_______________________________")

	resultList.clear()

print("Общее колличество сгенерированных элементов",globalCounter)