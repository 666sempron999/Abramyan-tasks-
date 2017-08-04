"""
Series21–. Дано целое число N (> 1) и набор из N вещественных чисел. Проверить, образует ли данный набор возрастающую последовательность. Если
образует, то вывести TRUE, если нет — вывести FALSE.
"""

import random

resultList = list()

N = int(input("Введите число элементов - "))

while N < 1:
	N = int(input("Введите число элементов - "))

for x in range(0,N):
	resultList.append(round((random.random() * 10),2))

print(resultList)

sortList = resultList[::]

sortList.sort()

print(sortList)

if sortList == resultList:
	print(True)
else:
	print(False)
	