# Выполнение задания
# Модуль 5. Часть 1. 
# Уровень 3-2*. 
# Бой трёх и более гладиаторов

from random import randint
import random 

class Gladiator():

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.endurance = 50
        self.armour = 20

    def hit(self):
        weakness = 10 * (self.endurance <= 0)
        hit_value = randint(10, 30-weakness)
        self.endurance -= 10
        return hit_value

    def receive_hit(self, hit_value, protected):
        if protected and self.armour >= 1:
            damage_value = randint(0,10)
            hit_value -= damage_value
            self.armour_damaged(damage_value)
            self.is_wounded(hit_value)
        else:
            self.is_wounded(hit_value)

    def armour_damaged(self, damage_value):
        self.armour -= damage_value
        if self.armour <= 0:
            self.armour = 0

    def is_wounded(self, heatlh_lost):
        self.health -= heatlh_lost
        if self.health <= 0:
            self.health = 0

    def is_alive(self):
        return (self.health >= 1)

class Arena():

    def __init__(self, name):
        self.gladiators = {}
        self.name = name 

    def add_gladiator(self, gladiator):
        self.gladiators[gladiator.name] = gladiator

    def run_fight(self):
        winner = None
        display_mode = {1:'attacks', 0:'defends'}

        while not winner:
            # Выбираем произвольную пару гладиаторов
            pair_names = random.sample(list(self.gladiators.keys()), 2)

            # Пара гладиаторов обменивается ударами
            attacks, slain = self.pair_combat_round(pair_names)
            print()
            print(pair_names[0], display_mode[attacks[0]], ' ', pair_names[1], display_mode[attacks[1]])
            if slain:
                print(slain, 'is dead')

            # Проверяем наличие гладиаторов на арене и определяем победителя
            winner = self.check_winner()

            # Выводим состояние здоровья гладиаторов на экран
            print('Gladiators left:', len(self.gladiators))
            for name, person in self.gladiators.items():
                print(name)
                print(person.health, person.armour, person.endurance)

        return winner

    def pair_combat_round(self, names):
        slain = None
        attacks = []

        for i in [0, 1]:
            attacks.append(randint(0, 1))               # 1 - атака, 0 - оборона
        both_attack = attacks[0] and attacks[1]
        if attacks[0]:
            slain = self.one_hit_other([names[0], names[1]], both_attack)
        if attacks[1] and not slain:
            slain = self.one_hit_other([names[1], names[0]], both_attack)
        if slain:
            self.gladiators.pop(slain)
            
        return attacks, slain

    def one_hit_other(self, names, both_attack):

        one, other = self.gladiators[names[0]], self.gladiators[names[1]]
        hit = one.hit()
        protected = not both_attack
        other.receive_hit(hit, protected)
        if not other.is_alive():
            slain = other.name
        else:
            slain = None 

        return slain
   
    def check_winner(self):
        winner = None          
        gladiators_left = len(self.gladiators)
        if gladiators_left == 1:
            gladiator = (list(self.gladiators.keys()))
            winner = gladiator[0]
        return winner

# Скрипт чемпионата
arenas = []
i = 0

arenas.append(Arena(name='Colosseum'))
arenas[i].add_gladiator(Gladiator('Spartacus'))
arenas[i].add_gladiator(Gladiator('Ajax'))
arenas[i].add_gladiator(Gladiator('Maximus'))
arenas[i].add_gladiator(Gladiator('Achilles'))
arenas[i].add_gladiator(Gladiator('Commodus'))

winners = []
winners.append(arenas[i].run_fight())
print(winners[i], 'wins at', arenas[i].name)




