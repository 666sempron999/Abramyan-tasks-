"""
Series16–. Дано целое число K и набор ненулевых целых чисел; признак
его завершения — число 0. Вывести номер последнего числа в наборе,
большего K. Если таких чисел нет, то вывести 0
"""
import random

resultList = list()

K = int(input("Введите число  - "))

pos = 0

for x in range(0,100):
	param = random.randint(-10, 10)
	if param != 0:
		resultList.append(param)

		if param > K:
			flag = True
			pos = x

	elif param == 0:
		resultList.append(param)
		break

print(resultList)
print("=========================================")

if pos != 0:
	print("Номер элемента, большего чем", K, "-", pos+1)
else:
	print(0)
