# Выполнение задания
# Модуль 4. Уровень 2.
# Реализация алгоритма сортировки вставками

# Алгоритмическая сложность: 
# по времени -- О(n^2) - два вложенных цикла (insertion_sort и insert_element)
# по памяти  -- O(n) - размер используемых массивов (sample, series) пропорционален числу элементов 

def swap_elements(series, i):									# O(1) по памяти и по времени					
	series[i], series[i-1] = series[i-1], series[i]				
	return series

def insert_element (series):									
	# все элементы в series отсортированы, кроме последнего, 
	# функция вставляет его куда надо 
	i = len(series)-1

	while i >= 1:												
		if series[i-1] > series[i]: 
			swap_elements(series, i)
		i -= 1
	return series

def insertion_sort(sample):										
	# Основная функция
	for n in range(1, len(sample)+1):							
		# print(sample[:n])
		sample[:n] = insert_element (sample[:n])				
	return sample

s = [0, 1, 11, 2, 3, 101, 4, 6, 7, 9, 8, 100, 100]
# s = [0]
print('Исходный массив:      ', s)
print('Сортированный массив: ', insertion_sort(s))
