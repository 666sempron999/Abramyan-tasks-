"""
Series6. Дано целое число N и набор из N положительных вещественных
чисел. Вывести в том же порядке дробные части всех чисел из данного набора (как вещественные числа с нулевой целой частью), а также
произведение всех дробных частей.
"""
import random
import math

N = int(input("Введите число элементов - "))

resultList = list()
floatList = list()

for x in range(0,N):
	resultList.append(round(random.random() * 100, 2))
	floatList.append((math.modf(resultList[x]))[0])

mul = 1

print(resultList)
print(floatList)

for i in range(0,len(floatList)):
	mul *= floatList[i]

print("____________________")
print("Произведение", mul)
