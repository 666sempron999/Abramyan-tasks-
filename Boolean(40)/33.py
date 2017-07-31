'''
Boolean33 ◦ . Даны целые числа a, b, c. Проверить истинность высказывания:
«Существует треугольник со сторонами a, b, c».
'''

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

flag = True

if a + b > c and b + c > a and c + a > b:
	pass
else:
	flag = False

print(flag)