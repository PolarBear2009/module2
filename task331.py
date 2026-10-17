# Выполнение задания
# Модуль 3. Часть 3. Уровень 1. 
# Вычисление площади треугольника по формуле Герона

def area (a,b,c):
	p = (a+b+c) / 2
	return ( p*(p-a)*(p-b)*(p-c) ) ** 0.5

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

s = area (a,b,c)
print ('Площадь: ', s)