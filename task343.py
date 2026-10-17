# Выполнение задания
# Модуль 3. Часть 4. Уровень 3.
# Вход в систему 

import json

def login_function (login, passwd):
	with open('logindata.json', 'r') as f:
		fdata = json.load(f)
	check = login in fdata.keys() and fdata[login] == passwd
	return check

login =  input('Имя пользователя: ')
passwd = input('          Пароль: ')

if login_function (login, passwd):
	print('Вход в систему выполнен.')
else:
	print('Ошибка! Неверное имя пользователя или пароль.')