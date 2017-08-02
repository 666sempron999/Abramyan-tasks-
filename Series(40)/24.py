"""
Series24. Дано целое число N и набор из N целых чисел, содержащий по
крайней мере два нуля. Вывести сумму чисел из данного набора, распо-
ложенных между последними двумя нулями (если последние нули идут
подряд, то вывести 0).
"""

import random
import sys

resultList = list()
zeroList = list()
summ = 0

N = int(input("Введите число элементов - "))

while N < 1:
	N = int(input("Введите число элементов - "))

for x in range(0,N):
	resultList.append(random.randint(0, 3))

print(resultList)

countZero = resultList.count(0)

if countZero < 2:
	print("Перезапустите программу!")
	exit()

elif countZero == 2:

	i = resultList.index(0)
	i += 1

	while resultList[i] != 0:
		summ += resultList[i]
		i += 1

elif countZero > 2:

	resultList.reverse()
	
	i = resultList.index(0)
	i += 1

	while resultList[i] != 0:
		summ += resultList[i]
		i += 1

print("Сумма между двумя последними нулями", summ)
