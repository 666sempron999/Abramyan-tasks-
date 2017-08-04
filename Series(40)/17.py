"""
Series17–. Дано вещественное число B, целое число N и набор из N вещественных чисел, упорядоченных по возрастанию. Вывести элементы
набора вместе с числом B, сохраняя упорядоченность выводимых чисел."""

import random

resultList = list()

B = float(input("Введите вещественное число - "))
N = int(input("Введите число элементов - "))

for x in range(0,N):
	resultList.append(round((random.random() * 10),1))

print(resultList)

resultList.sort()
print("_______________________________")

print(resultList)

print("_______________________________")

for i in range(0,len(resultList)):
	print(resultList[i])
	if resultList[i] < B and i < len(resultList) and resultList[i+1] > B:
		print("B -> ", B)

