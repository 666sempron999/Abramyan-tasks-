'''
Integer19 ◦ . С начала суток прошло N секунд (N — целое). Найти количество
полных минут, прошедших с начала суток
'''

N = int(input("Введите N: "))

minutes, seconds = divmod(N,60)

print('Chislo', N)
print(minutes)
