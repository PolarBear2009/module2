# Выполнение задания
# Модуль 5. Часть 1. 
# Уровень 3-2. 
# Бой гладиаторов

from random import randint
import random 

class Gladiator():

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.endurance = 50
        self.armour = 20
        self.position = []

    def hit(self, arena, target):
        weakness = 10 * (self.endurance <= 0)
        hit_value = randint(10, 30-weakness)
        if arena.protected[target]:
            hit_value -= 10
            damage_value = randint(0, 10) 
        else:
            damage_value = 0

        return hit_value, damage_value

    def armour_damaged(self, damage_value):
        self.armour -= damage_value
        if self.armour <= 0:
            self.armour = 0

    def is_wounded(self, hit_value):
        self.health -= hit_value
        if self.health <= 0:
            self.health = 0

class Arena():
    protected = []
    def __init__(self):
        for i in [0, 1]:
            self.protected.append(True)

    def combat_mode(self, gladiator):
        for i in [0, 1]:
            gladiator[i].position = randint(0, 1)   # 1 - атака, 0 - оборона

    def fatigue(self, gladiator):
        for i in [0, 1]:           
            if gladiator[i].position:
                gladiator[i].endurance -= 10

    def protection(self, gladiator): 
        for i in [0, 1]:
            if gladiator[i].armour >= 1: 
                self.protected[i] = not gladiator[i].position
            else:
                self.protected[i] = False    

    def check_winner(self, gladiator):           # тут проверка на арене
        enemy = [1, 0]
        for i in [0, 1]:
            if gladiator[i].health <= 10:
                winner = gladiator[enemy[i]].name
            else:
                winner = []
        return winner

# Morituri
gladiator = []
gladiator.append(Gladiator('Spartacus'))
gladiator.append(Gladiator('Ajax'))
print(gladiator[0].name, 'vs', gladiator[1].name, '\n')

# Начинаем...
print('Ave, Ceasar!\n')

arena = Arena()
enemy = [1, 0]  
winner = []

while not winner:

    arena.combat_mode(gladiator)            # определяем метод для каждого воина 
    arena.fatigue(gladiator)                # добавляем усталость 
    arena.protection(gladiator)             # проверяем наличие защиты
         
    for i in [0, 1]:
        print(gladiator[i].name, gladiator[i].health, gladiator[i].armour)

        if gladiator[i].position:
            print(gladiator[i].name, 'attacks')
            hit_value, damage_size = gladiator[i].hit(arena, enemy[i])
            gladiator[enemy[i]].armour_damaged(damage_size)
            gladiator[enemy[i]].is_wounded(hit_value)
            print(hit_value, damage_size)
        else:
            print(gladiator[i].name, 'defends')

    print()
    winner = arena.check_winner(gladiator)

print(winner, 'wins')
