'''
Integer11 ◦ . Дано трехзначное число. Найти сумму и произведение его цифр.
'''

A = int(input("Введите А: "))

while A > 999 or A < 100:
	print(A)
	A = int(input("Введите А: "))

sotni, des = divmod(A,100)

des, ed = divmod(des,10)

print('Chislo', A)
print("Summa - " ,sotni + des + ed)
print("Mul - " ,sotni * des * ed)