"""
Series8. Дано целое число N и набор из N целых чисел. Вывести в том же
порядке все четные числа из данного набора и количество K таких чисел.
"""
import random
import math

N = int(input("Введите число элементов - "))

resultList = list()


for x in range(0,N):
	resultList.append(random.randint(-100, 100))

print(resultList)
print("____________________")

positiveCount = 0

for i in range(0,len(resultList)):
	if resultList[i] > 0:
		positiveCount += 1
		print(resultList[i])


print("____________________")
print("Колличество положительных", positiveCount)
