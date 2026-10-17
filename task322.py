# Выполнение задания
# Модуль 3. Часть 2. Уровень 2. 

from random import randint

n = 5
m = [[ randint(0, 100) for i in range(n)] for j in range(n) ]
m1 = []

for q in m:
	# print(max(q))
	m1.append( max(q) )
	
print("Матрица: ", m)
print('Максимальное значение: ', max(m1))