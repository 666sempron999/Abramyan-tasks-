'''
For9. Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых
чисел от A до B включительно.
'''
import math as m


A = int(input("Введите A "))
B = int(input("Введите B "))

while A > B:
	A = int(input("Введите A "))
	B = int(input("Введите B "))

mul = 1

for i in range(A,B+1):
	print(i)
	mul += m.pow(i,2)

print(mul)