'''
Boolean35 ◦ . Даны координаты двух различных полей шахматной доски x 1 ,
y 1 , x 2 , y 2 (целые числа, лежащие в диапазоне 1–8). Проверить истинность
высказывания: «Данные поля имеют одинаковый цвет».
'''

x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))

x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

flag = True

color1 = ''
color2 = ''

if (x1 % 2 == 0 and y1 % 2 != 0) or (x1 % 2 != 0 and y1 % 2 == 0):
	color1 = 'white'
else:
	color1 = 'black'

if (x2 % 2 == 0 and y2 % 2 != 0) or (x2 % 2 != 0 and y2 % 2 == 0):
	color2 = 'white'
else:
	color2 = 'black'

if color1 == color2:
	pass
else:
	flag = False

print(flag)