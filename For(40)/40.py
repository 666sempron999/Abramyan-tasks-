'''
For40. Даны целые числа A и B (A < B). Вывести все целые числа от A до B
включительно; при этом число A должно выводиться 1 раз, число A + 1
должно выводиться 2 раза и т. д.
'''

A = int(input("Введите A "))
B = int(input("Введите B "))

while A > B:
	A = int(input("Введите A "))
	B = int(input("Введите B "))

counter = 1

for i in range(1,(B - A)+2):
	for j in range(1,counter + 1):
		print(A)

	print('---------')
	counter += 1
	A += 1

