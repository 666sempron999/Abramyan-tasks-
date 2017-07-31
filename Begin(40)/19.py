'''
Begin19 ◦ . Даны координаты двух противоположных вершин прямоугольника:
(x 1 , y 1 ), (x 2 , y 2 ). Стороны прямоугольника параллельны осям координат.
Найти периметр и площадь данного прямоугольника.
'''

x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

dlinna = abs(x2-x1)
visota = abs(y2-y1)

print("dlinna - ", dlinna, " visota - ", visota)

P = (dlinna + visota) * 2
S = dlinna * visota

print("Perimetr - ", P, " Plos - ", S)
