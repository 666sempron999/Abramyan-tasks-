'''
If21. Даны целочисленные координаты точки на плоскости. Если точка совпа-
дает с началом координат, то вывести 0. Если точка не совпадает с нача-
лом координат, но лежит на оси OX или OY, то вывести соответственно 1
или 2. Если точка не лежит на координатных осях, то вывести 3.
'''

x = int(input("Введите x: "))
y = int(input("Введите y: "))

result = 0

if x == y == 0:
	pass
elif x == 0 and y != 0:
	result = 1
elif x != 0 and y == 0:
	result = 2
else:
	result = 3

print(result)
