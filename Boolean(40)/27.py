'''
Boolean27 ◦ . Даны числа x, y. Проверить истинность высказывания: «Точка с
координатами (x, y) лежит во второй или третьей координатной четверти».
'''


x = int(input("Введите x: "))
y = int(input("Введите y: "))

flag = True

if (x < 0 and y > 0) or (x < 0 and y < 0):
	pass
else:
	flag = False

print(flag)