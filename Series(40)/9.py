"""
Series9. Дано целое число N и набор из N целых чисел. Вывести в том же
порядке номера всех нечетных чисел из данного набора и количество K
таких чисел.
"""
import random
import math

N = int(input("Введите число элементов - "))

resultList = list()


for x in range(0,N):
	resultList.append(random.randint(0, 100))

print(resultList)
print("____________________")

evenCount = 0

for i in range(0,len(resultList)):
	if resultList[i] % 2 == 0:
		evenCount += 1
		print(resultList[i])


print("____________________")
print("Колличество чётных", evenCount)
