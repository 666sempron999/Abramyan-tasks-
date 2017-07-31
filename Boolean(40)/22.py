'''
Boolean22 ◦ . Дано трехзначное число. Проверить истинность высказывания:
«Цифры данного числа образуют возрастающую или убывающую после-
довательность».
'''
"""
chislo - список из числа
sort - сортировка chislo

rev - перевёрнутый chislo
rev_sort - сортированый rev

"""

A = int(input("Введите A: "))

while A < 100 or A > 999:
	A = int(input("Введите A: "))

flag = True

chislo = list(str(A))

sort = chislo[:]

rev = chislo[:]

rev.reverse()

rev_sort = rev[:]
rev_sort.sort()

sort.sort()

if chislo == sort or rev == rev_sort:
	pass
else:
	flag = False

print(flag)