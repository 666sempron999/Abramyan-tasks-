"""
Series4. Дано целое число N и набор из N вещественных чисел. Вывести
сумму и произведение чисел из данного набора.
"""
import random
import math

N = int(input("Введите число элементов - "))

resultList = list()

for x in range(0,N):
	resultList.append(round(random.random() * 10, 2))

summa = 0
mul = 1

print(resultList)

for i in range(0,len(resultList)):
	summa += resultList[i]
	mul *= resultList[i]

print("____________________")
print("Сумма", summa)
print("____________________")
print("Произведение",mul)