'''
Begin36 ◦ . Скорость первого автомобиля V 1 км/ч, второго — V 2 км/ч, расстоя-
ние между ними S км. Определить расстояние между ними через T часов,
если автомобили удаляются друг от друга. Данное расстояние равно сум-
ме начального расстояния и общего пути, проделанного автомобилями;
общий путь = время · суммарная скорость.
'''

V1 = int(input("Vvedite skorost 1: "))
V2 = int(input("Vvedite skorost 2: "))
S = int(input("Rasstoyanie mejdu 1 i 2: "))
T = int(input("Vremya "))

S1 = V1 * T
S2 = V2 * T

print("Obchii put", S1 + S2 + S)
print("Obchii put v2", ((V1+V2)*T)+S)
