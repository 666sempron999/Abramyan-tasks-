'''
If23. Даны целочисленные координаты трех вершин прямоугольника, стороны
которого параллельны координатным осям. Найти координаты его четвертой вершины.
'1-я вершина - правый верхний угол, обход от первой вершины по часовой стрелке'
'''

x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))

x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

x3 = int(input("Введите x3: "))
y3 = int(input("Введите y3: "))

x4 = 0
y4 = 0

if x1 == x2 != x3 and y2 == y3 != y1:
	x4 = x3
	y4 = y1

print('x4 - ', x4)
print('y4 - ', y4)
