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
        self.armour = 100
        self.position = 'defend'

    def attack(self, enemy):
        self.position = 'attack'
        # если воин устал, маскисмальная сила удара уменьшается на величину weakness
        self.endurance -= 10    #   
        if self.endurance <= 0:
            weakness = 10           
        else:
            weakness = 0

        if enemy.position == 'defend' and enemy.armour >= 1:
            enemy.armour -= randint(0, 10)                      
            enemy.health -= (randint(0, 20 - weakness) )
        elif enemy.position == 'defend' and enemy.armour <= 1:
            enemy.health -= (randint(10, 30 - weakness) )            
        elif enemy.position == 'attack':
            enemy.health -= (randint(10, 30 - weakness) )
        else:
            print('Что-то пошло не так ...')

    def defend(self):
        self.position = 'defend'
        # по идее, тут воин должен отдыхать, но в описании этого нет


# Morituri
gladiator1 = Gladiator('Spartacus')
gladiator2 = Gladiator('Ajax')
print(gladiator1.name, 'vs', gladiator2.name, '\n')

# Начинаем...
print('Ave, Ceasar!\n')

winner = []

while not winner:
    # решение об атаке за каждого гладиатора(1 - атака, 0 - оборона)
    attack1 = randint(0,1)
    attack2 = randint(0,1)

    if attack1 and attack2:
        gladiator1.attack(gladiator2)
        gladiator2.attack(gladiator1)
    elif attack1 and (not attack2):
        gladiator2.defend()
        gladiator1.attack(gladiator2)
    elif (not attack1) and attack2:
        gladiator1.defend()
        gladiator2.attack(gladiator1)
    elif (not attack1) and (not attack2):
        gladiator1.defend()
        gladiator2.defend()


    print(gladiator1.name, end = ' ')
    print(gladiator1.position, 's', sep='')
    print('health:', gladiator1.health, end = '   ')
    print('armour:', gladiator1.armour, end = '   ')
    print('endurance:', gladiator1.endurance, end = '   ')
    print()
    print(gladiator2.name, end = ' ')
    print(gladiator2.position, 's', sep='')
    print('health:', gladiator2.health, end = '   ')
    print('armour:', gladiator2.armour, end = '   ')
    print('endurance:', gladiator2.endurance, end = '   ')
    print('\n')

    if gladiator1.health <= 10:
        winner = gladiator2.name
    elif gladiator2.health <= 10:
        winner = gladiator1.name

print(winner, 'wins')

spare = input('Pollice verso?')