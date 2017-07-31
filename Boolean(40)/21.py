'''
Boolean21 ◦ . Дано трехзначное число. Проверить истинность высказывания:
«Цифры данного числа образуют возрастающую последовательность».
'''

A = int(input("Введите A: "))

while A < 100 or A > 999:
	A = int(input("Введите A: "))

flag = True

chislo = list(str(A))

sort = chislo[:]

sort.sort()

if chislo == sort:
	pass
else:
	flag = False

print(flag)