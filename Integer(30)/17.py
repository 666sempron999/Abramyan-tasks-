'''
Integer17 ◦ . Дано целое число, большее 999. Используя одну операцию деле-
ния нацело и одну операцию взятия остатка от деления, найти цифру,
соответствующую разряду сотен в записи этого числа..
'''

A = int(input("Введите А: "))

while A < 999:
	print(A)
	A = int(input("Введите А: "))

sotni, des = divmod(A,100)

des, ed = divmod(des,10)

print('Chislo', A)
print(sotni)
