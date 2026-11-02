# Выполнение задания
# Модуль 5. Часть 1. 
# Уровень 1.   
# Создайте класс StringVar для работы со строковым типом данных, 
# содержащий методы set() и get(). Метод set() служит для изменения 
# содержимого строки, get() – для получения содержимого строки. Создайте 
# объект типа StringVar и протестируйте его методы.  


# Создаем класс 
class StringVar:
    # аттрибут
    string = ''
    
    # создаем методы класса 
    def __init__(self, s):
        self.string = s

    def set(self, s):
        self.string = s

    def get(self):
        return self.string

q = StringVar('Test string')
print(q.get())
q.set('New string')
print(q.get())
