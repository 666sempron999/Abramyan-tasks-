"""
Series20. Дано целое число N (> 1) и набор из N целых чисел. Вывести те
элементы в наборе, которые меньше своего правого соседа, и количество K
таких элементов.
"""

import random

resultList = list()

N = int(input("Введите число элементов - "))

while N < 1:
	N = int(input("Введите число элементов - "))

for x in range(0,N):
	resultList.append(random.randint(0, 10))

print(resultList)
print("_________________")

count = 0

for i in range(0,len(resultList)):
	if ((i < len(resultList)-1) and (resultList[i] < resultList[i+1])):
		print(resultList[i])
		count += 1

print("_________________")
print("Количество", count)
