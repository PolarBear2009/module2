# Выполнение задания
# Модуль 5. Часть 1. Уровень 2. 
# 
# Создается класс точка Point, позволяющий работать с координатами (x, y). 
# Методы класса: 
# 1) создание объекта, 
# 2) расстояние до начала координат
# 3) перемещение на вектор (dx, dy)
# 4) перевод (x, y) в полярные координаты
# 5) координаты середины отрезка между самой точкой и другой точкой

import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # расстояние до начала координат
    def distance_to_origin(self):
        x = self.x
        y = self.y
        return (x*x + y*y) ** (1/2)

    # смещение на вектор (dx,dy)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # полярные координаты
    def polar(self):                        
        rho = self.distance_to_origin()
        phi = math.atan(self.x / self.y)    # угол в радианах
        return rho, phi

    # координаты середины отрезка
    def get_midpoint_to(self, other):
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        return Point(x, y)


# Проверяем
a = Point(2, 0)
b = Point(0, 2)
a.move(1, 0)        # ползём вдоль оси абсцисс
b.move(0, 1)        # ползём вдоль оси ординат

c = a.get_midpoint_to(b)
print('Срединная точка:', 'x =', c.x, 'м, y =', c.y, 'м')

print('Её полярные координаты:')
rho, phi = c.polar()
print('Rho =', rho, 'метров.', 'Phi =', phi/math.pi*180, 'градусов')