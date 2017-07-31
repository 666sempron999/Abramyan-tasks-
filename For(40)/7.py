'''
For7. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел
от A до B включительно.
'''

A = int(input("Введите A "))
B = int(input("Введите B "))

while A > B:
	A = int(input("Введите A "))
	B = int(input("Введите B "))

summ = 0

for i in range(A,B+1):
	print(i)
	summ += i

print(summ)