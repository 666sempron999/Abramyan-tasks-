'''
Integer14 ◦ . Дано трехзначное число. В нем зачеркнули первую справа цифру
и приписали ее слева. Вывести полученное число.
'''

A = int(input("Введите А: "))

while A > 999 or A < 100:
	print(A)
	A = int(input("Введите А: "))

sotni, des = divmod(A,100)

des, ed = divmod(des,10)

print('Chislo', A)
print(str(ed) + str(des) + str(sotni))
