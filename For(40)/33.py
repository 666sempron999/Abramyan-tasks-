'''
For33 ◦ . Дано целое число N (> 1). Последовательность чисел Фибоначчи F K
(целого типа) определяется следующим образом:
F 1 = 1,
F 2 = 1,
F K = F K−2 + F K−1 , K = 3, 4, . . . .
Вывести элементы F 1 , F 2 , ..., F N .
'''

N = int(input("Введите N "))

while N <= 1:
	N = int(input("Введите N "))

Fp = 1
Fn = 1

print(Fp)
print(Fn)
summ = 0

for i in range(3,N+1):
	summ = Fp + Fn
	print(summ)
	Fp = Fn
	Fn = summ
