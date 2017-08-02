"""
Series13. Дан набор ненулевых целых чисел; признак его завершения — число 0. Вывести сумму всех положительных четных чисел из данного набора. Если требуемые числа в наборе отсутствуют, то вывести 0.
"""
import random

resultList = list()

summ = 0

for x in range(0,100):
	param = random.randint(-10, 10)
	if param != 0:
		resultList.append(param)
		if param > 0 and param % 2 == 0:
			summ += param

	elif param == 0:
		resultList.append(param)
		break

print(resultList)
print("=========================================")

if summ == 0:
	print(0)
else:
	print("Сумма положительных чётных", summ)
