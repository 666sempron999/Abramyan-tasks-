'''
Integer6 ◦ . Дано двузначное число. Вывести вначале его левую цифру (десят-
ки), а затем — его правую цифру (единицы). Для нахождения десятков
использовать операцию деления нацело, для нахождения единиц — опе-
рацию взятия остатка от деления.
'''

A = int(input("Введите А: "))

while A > 99 or A < 10:
	print(A)
	A = int(input("Введите А: "))

a,b = divmod(A,10)

print('Десятки - ',a)
print('Единицы - ',b)

