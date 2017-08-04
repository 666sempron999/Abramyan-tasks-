"""
Series28. Дано целое число N и набор из N вещественных чисел: A1, A2, : : :,
AN. Вывести следующие числа:
(A1)N, (A2)N¡1, : : :, (AN¡1)2, AN.
"""

import random

resultList = list()
degreeList = list()

N = int(input("Введите число элементов - "))

while N < 1:
	N = int(input("Введите число элементов - "))

mul = 1
decParam = N

for x in range(0,N):

	param = round((random.random() * 10),2)
	resultList.append(param)

	for j in range(0,decParam):
		mul *= param

	degreeList.append(mul)
	mul = 1
	decParam -= 1

print(resultList)
print(degreeList)
