"""
Series39. Дано целое число K, а также K наборов ненулевых целых чисел.
Каждый набор содержит не менее трех элементов, признаком его завер-
шения является число 0. Найти количество пилообразных наборов (опре-
деление пилообразного набора дано в задании Series23).
"""

import random

resultList = list()
countSaw = 0

N = int(input("Введите число элементов (оно равно и числу наборов) - "))

while N < 3:
	N = int(input("Введите число элементов - "))


print("_______________________________")

for i in range(1,N+1):

	for x in range(0,N):

		param = random.randint(0, 10)
		resultList.append(param)
		if param == 0:
			break

	print(resultList)

	for j in range(0,len(resultList),3):
		if i != 0 and i < len(resultList) - 2 and ((resultList[i-1] < resultList[i] and resultList[i] > resultList[i+1]) or (resultList[i-1] > resultList[i] and resultList[i] < resultList[i+1])):
			countSaw += 1

	print("количество зубцов",countSaw)
	countSaw = 0


	resultList.clear()
