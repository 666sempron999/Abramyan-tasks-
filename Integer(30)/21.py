'''
Integer21 ◦ . С начала суток прошло N секунд (N — целое). Найти количество
секунд, прошедших с начала последней минуты.
'''

N = int(input("Введите N: "))

minutes, seconds = divmod(N,60)

print('Chislo', N)
print(seconds)
