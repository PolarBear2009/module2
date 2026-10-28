# Выполнение задания
# Модуль 4. Уровень 1.
# Реализация алгоритма бинарного поиска

# Алгоритмическая сложность: 
# временная        -- О(log(n)) - количество элементов для поиска падает вдвое на каждом шаге
# пространственная -- О(log(n)) - размер стека рекурсии пропорционален log2(n)
# все операции сравнения и арифметические действия имеют сложность О(1) по времени и по памяти

def binary_search (series, key, low, high):

	if low > high:			# защита на случай, если элемента нет в массиве
		return []

	middle = (low + high) // 2 						
	if (series[middle] == key):						
		return (middle);
	elif (series[middle] > key):
		return (binary_search(series, key, low, middle-1))
	elif (series[middle] < key):
		return (binary_search(series, key, middle+1, high))


sample = [0, 1, 2, 3, 4, 6, 7, 8, 10, 100, 102]
print('Массив: ', sample)
key = float(input('Ключ: '))
# print('Ключ: ', key)

index = binary_search (sample, key, 0, len(sample) )

if index:
	print('Индекс:', index)
	print('Найденный элемент:', sample[index])
else:
	print('Ключ не найден!!')



