'''
Integer2 ◦ . Дана масса M в килограммах. Используя операцию деления нацело,
найти количество полных тонн в ней (1 тонна = 1000 кг).
'''

M = int(input("Введите число килограмм: "))

a,b = divmod(M,1000)

print('Количество тонн - ', a)
