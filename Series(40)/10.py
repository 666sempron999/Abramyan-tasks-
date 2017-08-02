"""
Series10. Дано целое число N и набор из N целых чисел. Если в наборе
имеются положительные числа, то вывести TRUE ; в противном случае
вывести FALSE .
"""
import random
import math

N = int(input("Введите число элементов - "))

resultList = list()


for x in range(0,N):
	resultList.append(random.randint(-100, 100))

print(resultList)
print("____________________")

for i in range(0,len(resultList)):
	if resultList[i] > 0:
		print(True)
		break


