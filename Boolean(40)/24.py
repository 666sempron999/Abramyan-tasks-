'''
Boolean24 ◦ . Даны числа A, B, C (число A не равно 0). Рассмотрев дискрими-нант D = B 2 − 4·A·C, проверить истинность высказывания: «Квадратное
уравнение A·x 2 + B·x + C = 0 имеет вещественные корни».
'''


A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

flag = True

while A == 0:
	A = int(input("Введите A: "))

D = B*B - (4 * A * C)

if D >= 0:
	pass
else:
	flag = False



print(flag)