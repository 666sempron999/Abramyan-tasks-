"""
Series11. Даны целые числа K, N и набор из N целых чисел. Если в наборе
имеются числа, меньшие K, то вывести TRUE ; в противном случае вывести
FALSE .
"""
import random
import math

N = int(input("Введите число элементов - "))
K = int(input("Введите число - "))

resultList = list()


for x in range(0,N):
	resultList.append(random.randint(0, 100))

print(resultList)
print("____________________")

trueFlag = False

for i in range(0,len(resultList)):
	if resultList[i] < K:
		print(True)
		trueFlag = True
		break

if trueFlag == False:
	print(False)


