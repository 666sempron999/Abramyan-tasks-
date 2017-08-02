"""
Series12. Дан набор ненулевых целых чисел; признак его завершения — число 0. 
Вывести количество чисел в наборе.
"""
import random

resultList = list()

for x in range(0,100):
	param = random.randint(-10, 10)
	if param != 0:
		resultList.append(param)
	elif param == 0:
		resultList.append(param)
		break

print(resultList)
print("=========================================")
print("Количество элементов", len(resultList))
