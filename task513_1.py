# Выполнение задания
# Модуль 5. Часть 1. 
# Уровень 3-1.

from random import randint

class Warrior():

    # создаем методы класса 
    def __init__(self, name):
        self.name = name
        self.health = 100

    def wounded(self):
        self.health -= 20
        if self.health <= 0:
            self.health = 0
            print(self.name, ' is slain')


# Combat
viking1 = Warrior('Sven')
viking2 = Warrior('Eric')


winner = []
while not winner:
    result = randint(1, 100) - 50
    # print(result)
    if result <= 0:
        print(viking2.name, 'hits')
        viking1.wounded()
        print(viking1.name, ':', viking1.health, 'health remain')
        if viking1.health <= 0:
            winner = viking2.name
    else:
        print(viking1.name, 'hits')
        viking2.wounded()
        print(viking2.name, ':', viking2.health, 'health remain')
        if viking2.health <= 0:
            winner = viking1.name

print(winner, 'wins')

