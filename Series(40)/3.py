"""
Series3. Даны десять вещественных чисел. Найти их среднее арифметическое.
"""
import random
import math


resultList = list()

count = 10

for x in range(0,count):
	resultList.append(round(random.random() * 10, 3))

summa = 0

for i in range(0,len(resultList)):
	print(resultList[i])
	if i != len(resultList)-1:
		print("+")
	summa += resultList[i]

print("____________________")
print(summa)
print("____________________")
print(summa/count)