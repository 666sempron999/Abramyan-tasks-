"""
Series38. Дано целое число K, а также K наборов ненулевых целых чисел.
Каждый набор содержит не менее двух элементов, признаком его завер-
шения является число 0. Для каждого набора выполнить следующее дей-
ствие: если элементы набора возрастают, то вывести 1; если элементы
набора убывают, то вывести −1; если элементы набора не возрастают и
не убывают, то вывести 0.
"""

import random

resultList = list()

globalCounter = 0
flag = False

N = int(input("Введите число элементов (оно равно и числу наборов) - "))

while N < 2:
	N = int(input("Введите число элементов - "))


print("_______________________________")

for i in range(1,N+1):

	for x in range(0,N):

		param = random.randint(0, 10)
		resultList.append(param)
		if param == 0:
			break

	print(resultList)

	buferList = resultList[::]
	buferList.sort()

	if resultList == buferList:
		print(1)
		flag = True

	buferList.clear()

	buferList = resultList[::]
	buferList.sort(reverse=True)

	if resultList == buferList:
		print(0)
		flag = True

	if flag == False:
		print("-1")

	buferList.clear()

	resultList.clear()
