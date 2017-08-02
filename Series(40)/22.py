"""
Series22. Дано целое число N (> 1) и набор из N вещественных чисел. Если
данный набор образует убывающую последовательность, то вывести 0;
в противном случае вывести номер первого числа, нарушающего закономерность.
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

sortList.sort(reverse=True)

print(sortList)

badIndex = 0

if sortList == resultList:
	print(0)
else:
	i = 0
	while resultList[i] > resultList[i+1] and (i < len(resultList) - 1):
		badIndex += 1
		i+=1

if badIndex != 0:
	print(badIndex)
