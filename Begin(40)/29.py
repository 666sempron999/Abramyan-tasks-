'''
Begin29 ◦ . Дано значение угла α в градусах (0 < α < 360). Определить значение
этого же угла в радианах, учитывая, что 180 ◦ = π радианов. В качестве
значения π использовать 3.14.
'''

import math as m

a = int(input("Угол a: "))
while a < 0 or a > 360:
        a = int(input("Угол a: "))
        
rad = a*(m.pi/180)

print("rad = ",rad)
