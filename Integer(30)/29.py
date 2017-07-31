'''
Integer28 ◦ . Дни недели пронумерованы следующим образом: 1 — понедель-
ник, 2 — вторник, . . . , 6 — суббота, 7 — воскресенье. Дано целое число K,
лежащее в диапазоне 1–365, и целое число N, лежащее в диапазоне 1–7.
Определить номер дня недели для K-го дня года, если известно, что в
этом году 1 января было днем недели с номером N
'''

A = int(input("Введите A: "))

B = int(input("Введите B: "))

C = int(input("Введите C: "))

while C > A or C > B:
	C = int(input("Введите C: "))

horisontal = A // C
print(horisontal)

vertical = B // C
print(vertical)

count =  horisontal * vertical

print('Count = ', count)

S = A * B

S1 = (C * C) * count

print('Ne zanyato - ', S - S1)