'''
If27. Для данного вещественного x найти значение следующей функции f,
принимающей значения целого типа:
				0, если x < 0,
f (x) =			1, если x принадлежит [0, 1), [2, 3), . . . ,
				−1, если x принадлежит [1, 2), [3, 4), . . . .
'''

x = float(input("Введите x: "))
fx = 0

if x < 0:
	fx = 0
elif (x >= 0 and x < 1) or (x >= 2 and x < 3):
	fx = 1
elif (x >= 1 and x < 2) or (x >= 3 and x < 4):
	fx = -1

print(fx)