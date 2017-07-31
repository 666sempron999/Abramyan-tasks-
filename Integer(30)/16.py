'''
Integer16 ◦ . Дано трехзначное число. Вывести число, полученное при переста-
новке цифр десятков и единиц исходного числа (например, 123 перейдет
в 132).
'''

A = int(input("Введите А: "))

while A > 999 or A < 100:
	print(A)
	A = int(input("Введите А: "))

sotni, des = divmod(A,100)

des, ed = divmod(des,10)

print('Chislo', A)
print(str(sotni) + str(ed) + str(des))
