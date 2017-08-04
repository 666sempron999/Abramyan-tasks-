"""
Series7. Дано целое число N и набор из N вещественных чисел. Вывести в
том же порядке округленные значения всех чисел из данного набора (как
целые числа), а также сумму всех округленных значений.
"""
import random
import math

N = int(input("Введите число элементов - "))

resultList = list()


for x in range(0,N):
	resultList.append(math.ceil(round(random.random() * 100, 2)))

summ = 0

for i in range(0,len(resultList)):
	summ += resultList[i]

print(resultList)

print("____________________")
print("Сумма", summ)
