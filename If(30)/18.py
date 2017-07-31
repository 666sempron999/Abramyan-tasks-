'''
If18. Даны три целых числа, одно из которых отлично от двух других, рав-
ных между собой. Определить порядковый номер числа, отличного от
остальных.
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

number = 0

if A != B and B == C:
	number = 1
elif B != C and C == A:
	number = 2
elif C != A and A == B:
	number = 3
else:
	number = "Error"

print('number - ', number)


