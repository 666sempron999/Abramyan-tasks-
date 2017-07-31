'''
Integer27 ◦ . Дни недели пронумерованы следующим образом: 1 — понедель-
ник, 2 — вторник, . . . , 6 — суббота, 7 — воскресенье. Дано целое число K,
лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня
года, если известно, что в этом году 1 января было субботой..
'''

K = int(input("Введите K: "))

while K > 365 or K < 0:
	K = int(input("Введите K: "))

weekDay = K % 7

if (weekDay + 5) > 7:
	weekDay = (weekDay + 5) - 7
else:
	weekDay = weekDay + 5

print(weekDay)