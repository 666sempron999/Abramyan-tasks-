'''
Begin7 ◦ . Найти длину окружности L и площадь круга S заданного радиуса R:
L = 2·π·R, S = π·R 2 .
В качестве значения π использовать 3.14.
'''
import math as m

r = int(input("Введите радиус окружности: "))


print("Длинна - ", 2 * m.pi * r)
print("Площадь - ", m.pi * pow(r,2))
