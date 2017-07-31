'''
For15 ◦ . Дано вещественное число A и целое число N (> 0). Найти A в степе-
ни N:
A N = A·A· . . . ·A
(числа A перемножаются N раз).
'''
A = int(input("Введите A "))
N = int(input("Введите N "))

while N <= 0:
	N = int(input("Введите N "))

mul = 1

for x in range(1,N+1):
	mul = mul * A

print(A,'^',N,'=',mul)