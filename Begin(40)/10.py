'''
Begin10 ◦ . Даны два ненулевых числа. Найти сумму, разность, произведение и
частное их квадратов.
'''

import math as m

a = int(input("Введите a: "))
while a == 0:
    a = int(input("Введите a: "))
    
b = int(input("Введите b: "))
while b == 0:
    b = int(input("Введите b: "))

print("Summa - ", pow(a,2) + pow(b,2))
print("Raznost - ", pow(a,2) - pow(b,2))
print("Proizvedenie - ", pow(a,2) * pow(b,2))
print("Chastnoe - ", pow(a,2) / pow(b,2))
