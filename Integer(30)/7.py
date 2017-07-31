'''
Integer7 ◦ . Дано двузначное число. Найти сумму и произведение его цифр.
'''

A = int(input("Введите А: "))

while A > 99 or A < 10:
	print(A)
	A = int(input("Введите А: "))

a,b = divmod(A,10)

print('Сумма - ', a + b)
print('Произведение - ', a * b)

