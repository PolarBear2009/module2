# Выполнение задания
# Модуль 5. Часть 1. 
# Уровень 3-1.
# Поединок викингов

from random import randint

class Warrior():

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 20
        self.alive = True

    def hit(self, other):
        other.is_wounded(self.strength)

    def attack(self, chance, other):
        result = randint(1, 100) - 100 + chance
        if result >= 0:
            self.hit(other)
            print(self.name, 'hits')
        else:
            print(self.name, 'missed')

    def is_wounded(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            
    def check_alive(self):
        if self.health == 0:
            self.alive = False
        return self.alive


# Поединок
viking = ['', '']
viking[0] = Warrior('Sven')
viking[1] = Warrior('Eric')
enemy = [1, 0]

chance = 50

winner = []
while not winner:
    for i in [0, 1]:
        viking[i].attack(chance, viking[enemy[i]])

        if viking[i].check_alive():
            print(viking[i].name, ':', viking[i].health, 'health remain')
        else:
            print(viking[i].name, 'is slain')
            winner = viking[enemy[i]].name
            break

print(winner, 'wins')

