"""
Series5. Дано целое число N и набор из N положительных вещественных
чисел. Вывести в том же порядке целые части всех чисел из данного
набора (как вещественные числа с нулевой дробной частью), а также
сумму всех целых частей
"""
import random
import math

N = int(input("Введите число элементов - "))

resultList = list()
intList = list()

for x in range(0,N):
	resultList.append(round(random.random() * 10, 2))
	intList.append(math.floor(resultList[x]))

summa = 0

print(resultList)
print(intList)

for i in range(0,len(intList)):
	summa += intList[i]

print("____________________")
print("Сумма", summa)
