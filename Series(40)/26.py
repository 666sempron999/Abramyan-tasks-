"""
Series26. Даны целые числа K, N и набор из N вещественных чисел: A1,
A2, : : :, AN. Вывести K-e степени чисел из данного набора:
(A1)K, (A2)K, : : :, (AN)K.
"""

import random

resultList = list()
degreeList = list()

N = int(input("Введите число элементов - "))

while N < 1:
	N = int(input("Введите число элементов - "))

K = int(input("Введите степень - "))
mul = 1

for x in range(0,N):

	param = round((random.random() * 10),2)
	resultList.append(param)

	for j in range(1,K+1):
		mul *= param

	degreeList.append(mul)
	mul = 1

print(resultList)
print(degreeList)
	
