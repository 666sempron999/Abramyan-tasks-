'''
Boolean18 ◦ . Проверить истинность высказывания: «Среди трех данных целых
чисел есть хотя бы одна пара совпадающих».
'''

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

flag = True

if(A == B or A == C or B ==C):
	pass
else:
	flag = False

print(flag)