'''
Begin23 ◦ . Даны переменные A, B, C. Изменить их значения, переместив содер-
жимое A в B, B — в C, C — в A, и вывести новые значения переменных A,
B, C
'''
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

a,b,c = c,a,b

print("a = ",a)
print("b = ",b)
print("c = ",c)