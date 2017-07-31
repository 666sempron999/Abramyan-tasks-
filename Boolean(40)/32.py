'''
Boolean32 ◦ . Даны целые числа a, b, c, являющиеся сторонами некоторого тре-
угольника. Проверить истинность высказывания: «Треугольник со сторо-
нами a, b, c является прямоугольным».
'''
import math as m

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if c < a:
	c,a = a,c
elif c < b:
	c,b = b,c

flag = True

if c == m.sqrt(a*a + b*b):
	pass
else:
	flag = False

print(flag)