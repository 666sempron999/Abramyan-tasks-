'''
For5 ◦ . Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1,
0.2, . . . , 1 кг конфет.
'''

A = int(input("Введите цену конфет за КГ: "))

for i in range(1,10):
	print((i/10)*A, 'р за',i/10, 'гр')
	