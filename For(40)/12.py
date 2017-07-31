'''
For12 ◦ . Дано целое число N (> 0). Найти произведение
1.1 · 1.2 · 1.3 · . . .
(N сомножителей)
'''
import math as m


N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

start = 1.1
mul = 1

for i in range(1,N):
	mul *= start
	start += 0.1

print(mul)