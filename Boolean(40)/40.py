'''
Boolean40 ◦ . Даны координаты двух различных полей шахматной доски x 1 ,
y 1 , x 2 , y 2 (целые числа, лежащие в диапазоне 1–8). Проверить истинность
высказывания: «Конь за один ход может перейти с одного поля на другое»
'''

def colorDefenition(x,y):

	if (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
		return 'white'
	else:
		return 'black'

def goAsHorse(x1,x2,y1,y2):
	pass

x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))

x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

flag = True

if colorDefenition(x1,y1) != colorDefenition(x2,y2):

	if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
		pass
	else:
		flag = False

else:
	flag = False

print(flag)