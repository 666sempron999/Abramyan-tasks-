"""
Case6. Единицы длины пронумерованы следующим образом: 1 — дециметр,
2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр. Дан номер
единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих
единицах (вещественное число). Найти длину отрезка в метрах.
"""
print('1 - дециметр')
print('2 - километр')
print('3 - метр')
print('4 - миллиметр')
print('5 - сантиметр')

A = int(input("Введите число: А - "))

C = int(input("Введите номер (1-5) - "))
while C > 5 or C < 1:
	C = int(input("Введите номер (1-5) - "))

result = 0

if C == 1:
	result = str(A * 10) + ' метров'
elif C == 2:
	result = str(A * 1000) + ' метров'
elif C == 3:
	result = str(A) + ' метров'
elif C == 4:
	result = str(A / 1000) + ' метров'
elif C == 5:
	result = str(A * 1000) + ' метров'


print(result)