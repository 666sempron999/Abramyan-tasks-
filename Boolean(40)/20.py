'''
Boolean20 ◦ . Дано трехзначное число. Проверить истинность высказывания:
«Все цифры данного числа различны».
'''

A = int(input("Введите A: "))

while A < 100 or A > 999:
	A = int(input("Введите A: "))

flag = True

a,b = divmod(A,100)
b,c = divmod(b,10)

if a != b and a != c and b != c:
	pass
else:
	flag = False

print(flag)