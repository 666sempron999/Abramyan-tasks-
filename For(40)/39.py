'''
For39. Даны целые положительные числа A и B (A < B). Вывести все целые
числа от A до B включительно; при этом каждое число должно выводиться
столько раз, каково его значение (например, число 3 выводится 3 раза).
'''

A = int(input("Введите A "))
B = int(input("Введите B "))

while A > B:
	A = int(input("Введите A "))
	B = int(input("Введите B "))

counter = A

for i in range(1,(B - A)+2):

	for j in range(1,counter+1):
		print(counter)

	print('---------')
	counter += 1
