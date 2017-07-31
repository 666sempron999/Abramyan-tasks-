"""
Case9–. Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года. Вывести значения D и M для даты,
следующей за указанной
"""

D = int(input("Введите число: D - "))
M = int(input("Введите число: M - "))

CountDay = 0

if M == 2:
	CountDay = 28
elif M == 4 or M == 6 or M == 9 or M == 11:
	CountDay = 30
elif M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
	CountDay = 31

if D < CountDay:
	D += 1
else:
	M = (M % 12) + 1
	D = 1

print(D)
print(M)
