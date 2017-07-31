'''
Begin12 ◦ . Даны катеты прямоугольного треугольника a и b. Найти его гипо-
тенузу c и периметр P:
c =
√ a 2
+ b 2 , P = a + b + c.
'''
import math as m

a = int(input("Введите a: "))
while a == 0:
    a = int(input("Введите a: "))
    
b = int(input("Введите b: "))
while b == 0:
    b = int(input("Введите b: "))
    
c = pow((pow(a,2) + pow(b,2)),(1/2))

print("Gipotenuza - ", c)
print("Perimetr - ", a + b +c)
