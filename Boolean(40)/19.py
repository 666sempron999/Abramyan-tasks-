'''
Boolean19 ◦ . Проверить истинность высказывания: «Среди трех данных целых
чисел есть хотя бы одна пара взаимно противоположных».
'''

A = int(input("Введите A: "))


flag = True

if(A == -B or A == -C or B == -A or B == -C or C == -A or C == -B):
	pass
else:
	flag = False

print(flag)