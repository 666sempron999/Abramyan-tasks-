'''
Begin35 ◦ . Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч
(U < V). Время движения лодки по озеру T 1 ч, а по реке (против течения)
— T 2 ч. Определить путь S, пройденный лодкой (путь = время · скорость).
Учесть, что при движении против течения скорость лодки уменьшается
на величину скорости течения.
'''

V = int(input("Vvedite skorost v stoyachei vode: "))
U = int(input("Skorost techenia: "))
T1 = int(input("T Po ozery: "))
T2 = int(input("T Protiv techenia: "))

S1 = V * T1
S2 = (V-U)*T2

print("Put po ozeru - ", S1)
print("Put po reke", S2)
