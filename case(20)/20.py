'''
Case20. Даны два целых числа: D (день) и M (месяц), определяющие пра-
вильную дату. Вывести знак Зодиака, соответствующий этой дате: «Водо-
лей» (20.1–18.2), «Рыбы» (19.2–20.3), «Овен» (21.3–19.4), «Телец» (20.4–
20.5), «Близнецы» (21.5–21.6), «Рак» (22.6–22.7), «Лев» (23.7–22.8), «Де-
ва» (23.8–22.9), «Весы» (23.9–22.10), «Скорпион» (23.10–22.11), «Стре-
лец» (23.11–21.12), «Козерог» (22.12–19.1).
'''

M = int(input("Введите месяц: "))

while M < 1 or M > 12:
	M = int(input("Введите месяц: "))

D = int(input("Введите день: "))

while D < 1 or D > 31:
	D = int(input("Введите день: "))

znak = ''

if (M == 1 or M == 2) and (D >= 20 or D <= 18):
	print('Водолей')
elif (M == 2 or M == 3) and (D >= 19 or D <= 20):
	print('Рыбы')
elif (M == 3 or M == 4) and (D >= 21 or D <= 19):
	print('Овен')
elif (M == 4 or M == 5) and (D >= 20 or D <= 20):
	print('Телец')
elif (M == 5 or M == 6) and (D >= 21 or D <= 21):
	print('Близнецы')
elif (M == 6 or M == 7) and (D >= 22 or D <= 22):
	print('Рак')
elif (M == 7 or M == 8) and (D >= 23 or D <= 22):
	print('Лев')
elif (M == 8 or M == 9) and (D >= 23 or D <= 22):
	print('Дева')
elif (M == 9 or M == 10) and (D >= 23 or D <= 22):
	print('Весы')
elif (M == 10 or M == 11) and (D >= 23 or D <= 22):
	print('Скорпион')
elif (M == 11 or M == 12) and (D >= 23 or D <= 21):
	print('Стрелец')
elif (M == 12 or M == 1) and (D >= 22 or D <= 19):
	print('Козерог')
