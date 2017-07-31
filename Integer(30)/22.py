'''
Integer22 ◦ . С начала суток прошло N секунд (N — целое). Найти количество
секунд, прошедших с начала последнего часа
'''

N = int(input("Введите N: "))

hours, seconds = divmod(N,3600)

print('Chislo', N)
print(seconds)
