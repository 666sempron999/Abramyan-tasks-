'''
Integer10 ◦ . Дано трехзначное число. Вывести вначале его последнюю цифру
(единицы), а затем — его среднюю цифру (десятки)
'''

A = int(input("Введите А: "))

while A > 999 or A < 100:
	print(A)
	A = int(input("Введите А: "))

a,b = divmod(A,100)

a,b = divmod(b,10)

print(b)

print(a)



