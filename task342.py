# Выполнение задания
# Модуль 3. Часть 4. Уровень 2.
# Проверяем, есть ли пользователь в системе, а если нет - регистрируем

import json

def register_user (login, passwd):
	# регистрация пользователя
	with open('logindata.json', 'r') as f:
		fdata = json.load(f)
		fdata[login] = passwd
	with open('logindata.json', 'w') as f:
		json.dump(fdata, f)

def check_login (login):
	# проверка на то, существует ли пользователь с таким логином в системе
	with open('logindata.json', 'r') as f:
		fdata = json.load(f)
	check = login in fdata.keys()
	return check

# Предполагается, что json-файл уже существует после выполнения уровня 1
login =  input('Login: ')
passwd = input('Password: ')

if check_login (login) == True:
	print ('User already exists')
else:
	register_user (login, passwd)