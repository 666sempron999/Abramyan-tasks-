'''
If8 ◦ . Даны два числа. Вывести вначале большее, а затем меньшее из них.
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A > B:
	print(A)
	print(B)
elif B > A:
	print(B)
	print(A)
else:
	pass
