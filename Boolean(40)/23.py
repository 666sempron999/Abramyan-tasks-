'''
Boolean23 ◦ . Дано четырехзначное число. Проверить истинность высказыва-
ния: «Данное число читается одинаково слева направо и справа налево».
'''


A = int(input("Введите A: "))

while A < 1000 or A > 9999:
	A = int(input("Введите A: "))

flag = True

chislo = list(str(A))

compare = chislo[::-1]

if chislo == compare:
	pass
else:
	flag = False

print(flag)