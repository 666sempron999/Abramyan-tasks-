"""
Series25. Дано целое число N и набор из N целых чисел, содержащий по
крайней мере два нуля. Вывести сумму чисел из данного набора, расположенных между первым и последним нулем (если первый и последний
нули идут подряд, то вывести 0).
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
	print("В сгенерированной последовательности мало нулей. Перезапустите программу!")
	exit()

elif countZero == 2:

	i = resultList.index(0)
	i += 1

	while resultList[i] != 0:
		summ += resultList[i]
		i += 1

elif countZero > 2:

	start = resultList.index(0)

	resultList.reverse()
	finish = len(resultList) - resultList.index(0)

	resultList.reverse()

	interestList = resultList[start:finish]
	
	summ = sum(interestList)

print("Сумма между крайними нулями", summ)
