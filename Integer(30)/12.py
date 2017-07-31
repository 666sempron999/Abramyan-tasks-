'''
Integer12 ◦ . Дано трехзначное число. Вывести число, полученное при прочте-
нии исходного числа справа налево.
'''

A = int(input("Введите А: "))

while A > 999 or A < 100:
	print(A)
	A = int(input("Введите А: "))

sotni, des = divmod(A,100)

des, ed = divmod(des,10)

print('Chislo', A)
print(str(ed) + str(des) + str(sotni))
