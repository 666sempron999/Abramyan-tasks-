'''
Begin32 ◦ . Дано значение температуры T в градусах Цельсия. Определить зна-
чение этой же температуры в градусах Фаренгейта. Температура по Цель-
сию T C и температура по Фаренгейту T F связаны следующим соотноше-
нием:
T C = (T F − 32)·5/9.
'''
TC = int(input("Введите температуру по цельсию: "))

TF = (TC/(5 / 9)) + 32

print("T = ",TF)