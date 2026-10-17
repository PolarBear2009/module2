# Выполнение задания
# Модуль 3. Часть 3. Уровень 3. 

# определим функцию, которая превращает список в число
def evaln (nums):
	s = ''
	for q in nums:
		s += str(q)
	return int(s)

# определим функцию, которая меняет местами два соседних элемента в списке
def exchange1 (nums, i):											
	nums[i+1], nums[i] = nums[i], nums[i+1]
	return nums

# определим основную функцию
def construct_max (nums):
	for j in range(0, len(nums)):
		for i in range(0, len(nums)-1):
			s0 = evaln (nums)
			# print('список = ', nums)
			nums = exchange1 (nums, i)
			if evaln (nums) <= s0:
				nums = exchange1 (nums, i)

	return evaln (nums)

# Проверяем, как работает
nums = [910, 218, 2, 31, 7, 900, 90, 991]		# список чисел
print ('Список:', nums)

m = construct_max (nums)
print ('Максимальное число:', m)