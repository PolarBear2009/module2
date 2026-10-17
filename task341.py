# Выполнение задания
# Модуль 3. Часть 4. Уровень 1.
# Создаем файл, в который будут записываться регистрационные данные,
# и регистрируем первого пользователя

import json

def register (login, passwd):
	with open('logindata.json', 'w') as f:
		json.dump({login: passwd}, f)

login  = input('Login:')
passwd = input('Password:')
register (login, passwd)