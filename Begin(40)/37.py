'''
Begin37 ◦ . Скорость первого автомобиля V 1 км/ч, второго — V 2 км/ч, расстоя-
ние между ними S км. Определить расстояние между ними через T часов,
если автомобили первоначально движутся навстречу друг другу. Данное
расстояние равно модулю разности начального расстояния и общего пути,
проделанного автомобилями; общий путь = время · суммарная скорость.
'''

V1 = int(input("Vvedite skorost 1: "))
V2 = int(input("Vvedite skorost 2: "))
S = int(input("Rasstoyanie mejdu 1 i 2: "))
T = int(input("Vremya "))

print("Obchii put ", abs(S - ((V1+V2)*T)))
