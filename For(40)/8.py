'''
For8. Даны два целых числа A и B (A < B). Найти произведение всех целых
чисел от A до B включительно.
'''

A = int(input("Введите A "))
B = int(input("Введите B "))

while A > B:
	A = int(input("Введите A "))
	B = int(input("Введите B "))

mul = 1

for i in range(A,B+1):
	print(i)
	mul *= i

print(mul)