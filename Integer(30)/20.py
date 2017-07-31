'''
Integer20 ◦ . С начала суток прошло N секунд (N — целое). Найти количество
полных часов, прошедших с начала суток.
'''

N = int(input("Введите N: "))

hours, minutes = divmod(N,3600)

print('Chislo', N)
print(hours)
