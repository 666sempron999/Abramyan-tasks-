'''
Integer24 ◦ . Дни недели пронумерованы следующим образом: 0 — воскресенье,
1 — понедельник, 2 — вторник, . . . , 6 — суббота. Дано целое число K,
лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня
года, если известно, что в этом году 1 января было понедельником
'''

K = int(input("Введите K: "))

weekDay = K % 7

print(weekDay)
