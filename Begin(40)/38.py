'''
Begin38 ◦ . Решить линейное уравнение A·x + B = 0, заданное своими коэффи-
циентами A и B (коэффициент A не равен 0)
'''

A = int(input("Введите A: "))
while A == 0:
    A = int(input("Введите A: "))

B = int(input("Введите B: "))

X = -B/A

print(X)
