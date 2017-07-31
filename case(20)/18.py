'''
Case18. Дано целое число в диапазоне 100–999. Вывести строку-описание
данного числа, например: 256 — «двести пятьдесят шесть», 814 — «во-
семьсот четырнадцать».
'''

N = int(input("Введите цифру: "))
while N < 99 or N > 999:
	N = int(input("Введите цифру: "))

sotni = ''
des = ''
ed = ''

sotni,des = divmod(N,100)
des,ed = divmod(des,10)

print(sotni, ' ', des, ' ', ed)

if ed == 1:
	ed = ' один'

elif ed == 2:
	ed = ' два'

elif ed == 3:
	ed = ' три'

elif ed == 4:
	ed = ' четыре'

elif ed == 5:
	ed = ' пять'

elif ed == 6:
	ed = ' шесть'

elif ed == 7:
	ed = ' семь'

elif ed == 8:
	ed = ' восемь'

elif ed == 9:
	ed = ' девять'

'''
'''
if sotni == 1:
	sotni = 'Сто '

elif sotni == 2:
	sotni = 'Двести '

elif sotni == 3:
	sotni = 'Триста '

elif sotni == 4:
	sotni = 'Четыриста '

elif sotni == 5:
	sotni = 'Пятьсот '

elif sotni == 6:
	sotni = 'Шастьсот '

elif sotni == 7:
	sotni = 'Семсот '

elif sotni == 8:
	sotni = 'Восемсот '

elif sotni == 9:
	sotni = 'Девятьсот '

'''
'''
if des == 1 and ed == 0:
	des = 'десять'
	ed = ''

if des == 1 and ed == 1:
	des = 'одинадцать'
	ed = ''

elif des == 1 and ed == 2:
	des = 'двенадцать'
	ed = ''

elif des == 1 and ed == 3:
	des = 'тринадцать'
	ed = ''

elif des == 1 and ed == 4:
	des = 'четырнадцать'
	ed = ''

elif des == 1 and ed == 5:
	des = 'пятнадцать'
	ed = ''

elif des == 1 and ed == 6:
	des = 'шестнадцать'
	ed = ''

elif des == 1 and ed == 7:
	des = 'семнадцать'
	ed = ''

elif des == 1 and ed == 8:
	des = 'восемнадцать'
	ed = ''

elif des == 1 and ed == 9:
	des = 'девятнадцать'
	ed = ''

'''
'''
if des == 2 and ed == 0:
	des = 'двадцать'
	ed = ''
elif des == 2:
	des = 'двадцать'

if des == 3 and ed == 0:
	des = 'тридцать'
	ed = ''
elif des == 3:
	des = 'тридцать'

if des == 4 and ed == 0:
	des = 'сорок'
	ed = ''
elif des == 4:
	des = 'сорок'

if des == 5 and ed == 0:
	des = 'пятдесят'
	ed = ''
elif des == 5:
	des = 'пятдесят'

if des == 6 and ed == 0:
	des = 'шестдесят'
	ed = ''
elif des == 6:
	des = 'шестдесят'

if des == 7 and ed == 0:
	des = 'семдесят'
	ed = ''
elif des == 7:
	des = 'семдесят'

if des == 8 and ed == 0:
	des = 'восемдесят'
	ed = ''
elif des == 8:
	des = 'восемдесят'

if des == 9 and ed == 0:
	des = 'девяносто'
	ed = ''
elif des == 9:
	des = 'девяносто'

'''
'''
print(sotni,des,ed)