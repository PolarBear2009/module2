# Выполнение задания
# Модуль 3. Часть 2. Уровень 3. 
# 
# Исходный словарь называется capital_by_country
# Словарь, у которого ключи и значения поменяны местами, называется country_by_capital

capital_by_country = {
'Россия': 'Москва',
'США': 'Вашингтон',
'Китай': 'Пекин',
}

country_by_capital = {'': ''}		# создаем словарь с пустым ключом

for country, capital in capital_by_country.items():
	country_by_capital[capital] = country

country_by_capital.pop('')									# удаляем "пустой" ключ

print('Измененный словарь:', country_by_capital)			# готово!
