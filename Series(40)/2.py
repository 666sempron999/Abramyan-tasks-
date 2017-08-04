"""
Series2. Даны десять вещественных чисел. Найти их произведение.
"""
import random
import math


resultList = list()


for x in range(1,11):
	resultList.append(round(random.random() * 10, 3))

mul = 1

for i in range(0,len(resultList)):
	print(resultList[i])
	if i != len(resultList)-1:
		print("*")
	mul *= resultList[i]

print("____________________")
print(mul)
