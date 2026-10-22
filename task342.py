# Выполнение задания
# Модуль 3. Часть 4. Уровень 2.
# Проверяем, есть ли пользователь в системе, а если нет - регистрируем

import json

def register_user (login, passwd):
	# регистрация пользователя
	with open('logindata.json', 'r') as f:
		fdata = json.load(f)
		if login in fdata.keys():
			print ('User already exists')
		else:
			fdata[login] = passwd
	with open('logindata.json', 'w') as f:
		json.dump(fdata, f)


# Предполагается, что json-файл уже существует после выполнения уровня 1
login =  input('Login: ')
passwd = input('Password: ')
register_user (login, passwd)