'''
Boolean31 ◦ . Даны целые числа a, b, c, являющиеся сторонами некоторого тре-
угольника. Проверить истинность высказывания: «Треугольник со сторо-
нами a, b, c является равнобедренным».
'''

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))


flag = True

if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
	pass
else:
	flag = False
print(flag)