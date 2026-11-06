# Выполнение задания
# Модуль 5. Часть 1. 
# Уровень 3-1.

from random import randint

class Warrior():

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.alive = True

    def attack(self, other, strength):
        other.is_wounded(strength)

    def is_wounded(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            
    def check_alive(self):
        if self.health == 0:
            self.alive = False
        return self.alive


# Combat
viking1 = Warrior('Sven')
viking2 = Warrior('Eric')
strength = 20;

winner = []
while not winner:
# for i in range(10):
    result = randint(1, 100) - 50

    if result <= 0:
        print(viking2.name, 'hits')
        viking2.attack(viking1, strength)
        if viking1.check_alive():
            print(viking1.name, ':', viking1.health, 'health remain')
            # print(viking1.name, viking1.check_alive())
        else:
            print(viking1.name, 'is slain')
            winner = viking2.name
    else:
        print(viking1.name, 'hits')
        viking1.attack(viking2, strength)
        if viking2.check_alive():
            print(viking2.name, ':', viking2.health, 'health remain')
            # print(viking2.name, viking2.check_alive())
        else:
            print(viking2.name, 'is slain')
            winner = viking1.name

print(winner, 'wins')

