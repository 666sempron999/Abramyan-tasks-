'''
For6. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2,
1.4, . . . , 2 кг конфет.
'''

A = int(input("Введите цену конфет за КГ: "))

for i in range(1,10):
	print((i/10)*A + A, 'р за',1 + i/10, 'гр')