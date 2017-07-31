'''
Case19. В восточном календаре принят 60-летний цикл, состоящий из 12-
летних подциклов, обозначаемых названиями цвета: зеленый, красный,
желтый, белый и черный. В каждом подцикле годы носят названия живот-
ных: крысы, коровы, тигра, зайца, дракона, змеи, лошади, овцы, обезьяны,
курицы, собаки и свиньи. По номеру года определить его название, если
1984 год — начало цикла: «год зеленой крысы».
'''

N = int(input("Введите год: "))
while N < 1984:
	N = int(input("Введите год: "))

years = N - 1984
sycles,subsycles = divmod(years,60)

number, year = divmod(subsycles, 12)

sub = ''
animal = ''

if number == 1:
	sub = 'зелёный'

elif number == 2:
	sub = 'красный'

elif number == 3:
	sub = 'жёлтый'

elif number == 4:
	sub = 'белый'

else:
	sub = 'чёрный'

if year == 1:
	animal = ''

elif year == 2:
	animal = ''

elif year == 3:
	animal = ''

elif year == 4:
	animal = ''

elif year == 5:
	animal = ''

elif year == 6:
	animal = ''

elif year == 7:
	animal = ''

elif year == 8:
	animal = ''

elif year == 9:
	animal = ''

elif year == 10:
	animal = ''

elif year == 11:
	animal = ''

elif year == 12:
	animal = ''


print('год ', sub, animal)