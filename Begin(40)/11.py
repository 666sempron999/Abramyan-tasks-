'''
Begin11 ◦ . Даны два ненулевых числа. Найти сумму, разность, произведение и
частное их модулей.
'''

import math as m

a = int(input("Введите a: "))
while a == 0:
    a = int(input("Введите a: "))
    
b = int(input("Введите b: "))
while b == 0:
    b = int(input("Введите b: "))

a = abs(a)
b = abs(b)

print("Summa - ", a + b)
print("Raznost - ", a - b)
print("Proizvedenie - ",a * b)
print("Chastnoe - ", a / b)
