"""
Series18. Дано целое число N и набор из N целых чисел, упорядоченный
по возрастанию. Данный набор может содержать одинаковые элементы.
Вывести в том же порядке все различные элементы данного набора.
"""

import random

resultList = list()

N = int(input("Введите число элементов - "))

for x in range(0,N):
	resultList.append(random.randint(0, 10))

print(resultList)

resultList.sort()
print("_______________________________")

print(resultList)

print("_______________________________")

print(set(resultList))
