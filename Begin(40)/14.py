'''
Begin14 ◦ . Дана длина L окружности. Найти ее радиус R и площадь S круга,
ограниченного этой окружностью, учитывая, что L = 2·π·R, S = π·R 2 . В
качестве значения π использовать 3.14.
'''
import math as m

L = int(input("Введите L: "))
while L == 0:
    L = int(input("Введите L: "))
    
R = L / (2*m.pi)
S = m.pi * pow(R,2)

print("R = ",R)
print("S = ",S)
