"""
Series14. Дано целое число K и набор ненулевых целых чисел; признак его
завершения — число 0. Вывести количество чисел в наборе, меньших K.
"""
import random

resultList = list()

K = int(input("Введите число  - "))

count = 0

for x in range(0,100):
	param = random.randint(-10, 10)
	if param != 0:
		resultList.append(param)
		if param < K:
			count += 1

	elif param == 0:
		resultList.append(param)
		break

print(resultList)
print("=========================================")

print("Количество чисел меньше",K, "-", count)
