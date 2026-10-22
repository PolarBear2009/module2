# Выполнение задания
# Модуль 3. Часть 4. Уровень 1.
# Создаем файл, в который будут записываться регистрационные данные,
# и регистрируем первых пользователей

import json

def register_user (login, passwd):
	with open('logindata.json', 'r') as f:
		fdata = json.load(f)
		fdata[login] = passwd
	with open('logindata.json', 'w') as f:
		json.dump(fdata, f)

begin = {'dummy_user': 'dummy_pwd'}
with open('logindata.json', 'w') as f:
		json.dump(begin, f)

for user in [1, 2]:
	print ('User', user)
	login  = input('Login:')
	passwd = input('Password:')
	register_user (login, passwd)