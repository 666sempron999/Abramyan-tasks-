"""
Case10. Робот может перемещаться в четырех направлениях («С» — север,
«З» — запад, «Ю» — юг, «В» — восток) и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, ¡1 — поворот
направо. Дан символ C — исходное направление робота и целое число N
— посланная ему команда. Вывести направление робота после выполнения полученной команды.
"""
print('1 Север')
print('2 Запад')
print('3 Юг')
print('4 Восток')

C = int(input("Исходное направление - "))

print('0 - продолжать движение')
print('1 - поворот налево')
print('-1 - поворот направо')

N = int(input("Посланая команда - "))

napravlenie = ''

if C == 1 and N == 0:
	napravlenie == 'Север'
elif C == 1 and N == 1:
	napravlenie == 'Восток'
elif C == 1 and N == -1:
	napravlenie == 'Запад'

if C == 2 and N == 0:
	napravlenie == 'Запад'
elif C == 2 and N == 1:
	napravlenie == 'Север'
elif C == 2 and N == -1:
	napravlenie == 'Юг'

if C == 3 and N == 0:
	napravlenie == 'Юг'
elif C == 3 and N == 1:
	napravlenie == 'Запад'
elif C == 3 and N == -1:
	napravlenie == 'Восток'

if C == 4 and N == 0:
	napravlenie == 'Восток'
elif C == 4 and N == 1:
	napravlenie == 'Юг'
elif C == 4 and N == -1:
	napravlenie == 'Север'

print(napravlenie)