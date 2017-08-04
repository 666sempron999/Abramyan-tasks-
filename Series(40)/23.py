"""
Series23. Дано целое число N (> 2) и набор из N вещественных чисел. Набор
называется пилообразным, если каждый его внутренний элемент либо
больше, либо меньше обоих своих соседей (то есть является «зубцом»).
Если данный набор является пилообразным, то вывести 0; в противном
случае вывести номер первого элемента, не являющегося зубцом.
"""

import random

resultList = list()

N = int(input("Введите число элементов - "))

while N < 2:
	N = int(input("Введите число элементов - "))

for x in range(0,N):
	resultList.append(round((random.random() * 10),2))

print(resultList)

for i in range(0,len(resultList)):
	if i != 0 and i < len(resultList) - 2 and ((resultList[i+1] > resultList[i] and resultList[i+1] > resultList[i+2]) or (resultList[i+1] < resultList[i] and resultList[i+1] < resultList[i+2])):
		print(0)
	else:
		print(resultList[i])
