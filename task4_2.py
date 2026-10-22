# Выполнение задания
# Модуль 4. Уровень 2.

def swap_elements(series, i):											
	series[i], series[i-1] = series[i-1], series[i]
	return series

def insert_element (series):
	# все элементы в series отсортированы, кроме последнего, 
	# функция вставляет его куда надо 
	i = len(series)-1
	while (series[i-1] > series[i] and i > 0):
		swap_elements(series, i)
		i -= 1
	return series

def insertion_sort(sample):
	# Основная функция
	for n in range(1, len(sample)+1):
		# print(sample[:n])
		sample[:n] = insert_element (sample[:n])
	return sample

s = [0, 1, 11, 2, 3, 101, 4, 6, 7, 9, 8, 10, 100]
print('Исходный массив:      ', s)
print('Сортированный массив: ', insertion_sort(s))
