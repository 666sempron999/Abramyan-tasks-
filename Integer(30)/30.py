'''
Integer30 ◦ . Дан номер некоторого года (целое положительное число). Опре-
делить соответствующий ему номер столетия, учитывая, что, к примеру,
началом 20 столетия был 1901 год.
'''

A = int(input("Введите А: "))

a,b = divmod(A,100)

if b > 0:
	a = a+1
print(a)
