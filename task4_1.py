# Выполнение задания
# Модуль 4. Уровень 1.

def binary_search (series, key, low, high):

	middle = (low + high) // 2
	if (series[middle] == key):
		return (middle);
	elif (series[middle] > key):
		return (binary_search(series, key, low, middle-1))
	elif (series[middle] < key):
		return (binary_search(series, key, middle+1, high))

sample = [0, 1, 2, 3, 4, 6, 7, 8, 10, 100, 102]
key = 8
index = binary_search (sample, key, 0, len(sample) )
print('Массив: ', sample)
print('Ключ: ', key)
print('Индекс:', index)
print('Найденный элемент:', sample[index])
