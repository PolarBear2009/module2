# Выполнение задания
# Модуль 3. Часть 1. Уровень 1. 

x = float(input ('начальный вклад: '))
p = float(input ('годовой процент: '))
y = float(input ('надо накопить: '))

current_year = 0

while (x < y):
	x = x * (1 + p/100)
	x = int(x*100) / 100
	print('вклад: ', int(x), ' рублей', round((x-int(x))*100.), ' копеек')
	current_year += 1

print('Прошло лет: ', current_year)