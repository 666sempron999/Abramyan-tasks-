"""
Series36. Дано целое число K, а также K наборов ненулевых целых чисел.
Каждый набор содержит не менее двух элементов, признаком его завер-
шения является число 0. Найти количество наборов, элементы которых
возрастают.
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

	for j in range(0,len(resultList)):
		if (j < len(resultList)-1) and (resultList[j] > resultList[j+1]): 
			flag = False
			break
		elif (j < len(resultList)-1) and (resultList[j] < resultList[j+1]):
			flag = True

	
	if flag == True:
		globalCounter += 1

	resultList.clear()

print("Число возрастающих массивов",globalCounter)