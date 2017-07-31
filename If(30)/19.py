'''
If19. Даны четыре целых числа, одно из которых отлично от трех других,
равных между собой. Определить порядковый номер числа, отличного от
остальных.
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

number = 0

if A != B and B == C == D:
	number = 1
elif B != C and C == D == A:
	number = 2
elif C != D and D == A == B:
	number = 3
elif D != A and A == B == C:
	number = 4
else:
	number = "Error"

print('number - ', number)


