'''
Case15. Мастям игральных карт присвоены порядковые номера: 1 — пики,
2 — трефы, 3 — бубны, 4 — червы. Достоинству карт, старших десятки,
присвоены номера: 11 — валет, 12 — дама, 13 — король, 14 — туз. Даны
два целых числа: N — достоинство (6 ≤ N ≤ 14) и M — масть карты
(1 ≤ M ≤ 4). Вывести название соответствующей карты вида «шестерка
бубен», «дама червей», «туз треф» и т. п.
'''

import math as m

N = int(input("Введите достоинство карты: "))
while N <= 6 or N >= 14:
	N = int(input("Введите достоинство карты: "))

o = int(input("Введите масть карты (1 - пики, 2 - трефы, 3 - бубны, 4 - червы): "))
while o <= 1 or o >= 4:
	o = int(input("Введите масть карты (1 - пики, 2 - трефы, 3 - бубны, 4 - червы): "))


if N == 6:
	N = 'Шесть'

elif N == 7:
	N = 'Семь'

elif N == 8:
	N = 'Восемь'

elif N == 9:
	N = 'Девять'

elif N == 10:
	N = 'Десять'

elif N == 11:
	N = 'Валет'

elif N == 12:
	N = 'Дама'

elif N == 13:
	N = 'Король'

elif N == 14:
	N = 'Туз'

if o == 1:
	o = ' пики'

elif o == 2:
	o = ' трефы'

elif o == 3:
	o = ' бубны'

elif o == 4:
	o = ' червы'

print(N + o)