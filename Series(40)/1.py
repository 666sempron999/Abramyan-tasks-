"""
Series1–. Даны десять вещественных чисел. Найти их сумму
"""
import random

resultList = list()

for x in range(1,11):
	resultList.append(random.randint(1, 100))

summa = 0

for i in range(0,len(resultList)):
	print(resultList[i])
	if i != len(resultList)-1:
		print("+")
	summa += resultList[i]

print("____________________")
print(summa)
