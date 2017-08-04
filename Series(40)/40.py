"""
Series40. Дано целое число K, а также K наборов ненулевых целых чисел.
Каждый набор содержит не менее трех элементов, признаком его завер-
шения является число 0. Для каждого набора выполнить следующее дей-
ствие: если набор является пилообразным (см. задание Series23), то выве-
сти количество его элементов; в противном случае вывести номер первого
элемента, который не является зубцом.
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

	for i in range(0,len(resultList)):
		if i != 0 and i < len(resultList) - 2:
			if resultList[i+1] > resultList[i] and resultList[i+1] > resultList[i+2]:
				countSaw += 1
			elif resultList[i+1] < resultList[i] and resultList[i+1] < resultList[i+2]:
				countSaw += 1
			else:
				print("Это не пилообразная последовательность!")
				break

	print("количество зубцов",countSaw)
	countSaw = 0


	resultList.clear()
