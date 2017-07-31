'''
If22 . Даны координаты точки, не лежащей на координатных осях OX и OY.
Определить номер координатной четверти, в которой находится данная
точка
'''

x = int(input("Введите x: "))
y = int(input("Введите y: "))

result = 0

if x == y == 0 or x == 0 or y == 0:
	pass
elif x > 0 and y > 0:
	result = 1
elif x < 0 and y > 0:
	result = 2
elif x < 0 and y < 0:
	result = 3
elif x > 0 and y < 0:
	result = 4

print(result)
