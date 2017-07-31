'''
Boolean39 ◦ . Даны координаты двух различных полей шахматной доски x 1 , y 1 ,
x 2 , y 2 (целые числа, лежащие в диапазоне 1–8). Проверить истинность вы-
сказывания: «Ферзь за один ход может перейти с одного поля на другое».
'''

def colorDefenition(x,y):

	if (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
		return 'white'
	else:
		return 'black'

def goAsLad(x1,x2,y1,y2):

	if x1 == x2 or y1 == y2:
		return True
	else:
		return False

def goAsEl(x1,x2,y1,y2):

	if (abs(x1 - x2)) == (abs(y1 - y2)):
		return True
	else:
		return False

x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))

x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

flag = True

if colorDefenition(x1,y1) == colorDefenition(x2,y2):

	if goAsLad(x1,x2,y1,y2):
		pass

	elif goAsEl(x1,x2,y1,y2):
		pass
	else:
		flag = False

else:
	flag = False

print(flag)