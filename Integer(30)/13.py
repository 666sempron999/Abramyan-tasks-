'''
Integer13 ◦ . Дано трехзначное число. В нем зачеркнули первую слева цифру и
приписали ее справа. Вывести полученное число
'''

A = int(input("Введите А: "))

while A > 999 or A < 100:
	print(A)
	A = int(input("Введите А: "))

sotni, des = divmod(A,100)

des, ed = divmod(des,10)

print('Chislo', A)
print(str(des) + str(ed) + str(sotni))
