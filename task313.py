# Выполнение задания
# Модуль 3. Часть 1. Уровень 3. 

x = input ('Введите число: ')

sum_dig1 = 0

for i in range(0, len(x)):
	# print(x[i])
	sum_dig1 += int(x[i])
	
print('Сумма цифр:', sum_dig1)