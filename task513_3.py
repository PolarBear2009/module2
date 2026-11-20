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
        self.gladiators = []
        self.name = name 

    def add_gladiator(self, gladiator):
        self.gladiators.append(gladiator)

    def select_random_pair(self):
        numbers = range(len(self.gladiators))
        list_of_gladiators = [self.gladiators[i].name for i in numbers]
        morituri1 = random.choice(list_of_gladiators)
        list_of_gladiators.remove(morituri1)
        morituri2 = random.choice(list_of_gladiators)
        list_of_gladiators.remove(morituri2)
        pair_names = [morituri1, morituri2]
        return pair_names

    def run_fight(self):
        winner = []
        display_mode = {1:'attacks', 0:'defends'}

        while not winner:
            # Выбираем произвольную пару гладиаторов
            names = self.select_random_pair()

            # Пара гладиаторов обменивается ударами
            attacks, slain = self.pair_combat_round(names)
            print()
            print(names[0], display_mode[attacks[0]], ' ', names[1], display_mode[attacks[1]])
            if slain:
                print(slain, 'is dead')

            # Проверяем наличие гладиаторов на арене и определяем победителя
            winner = arena.check_winner()
            print('Gladiators left:', len(self.gladiators))

            # Выводим состояние здоровья гладиаторов на экран
            for i in range(len(self.gladiators)):
                print(arena.gladiators[i].name)
                print(arena.gladiators[i].health, arena.gladiators[i].armour, arena.gladiators[i].endurance)

        return winner

    def pair_combat_round(self, names):
        slain = []
        attacks = [''] * 2

        for i in [0, 1]:
            attacks[i] = randint(0, 1)               # 1 - атака, 0 - оборона
        both_attack = attacks[0] and attacks[1]
        if attacks[0]:
            slain = self.one_hit_other([names[0], names[1]], both_attack)
        if attacks[1] and not slain:
            slain = self.one_hit_other([names[1], names[0]], both_attack)
        if slain:
            self.remove_gladiator(slain)
            
        return attacks, slain

    def one_hit_other(self, pair_names, both_attack):
        slain = [] 

        attacker, defender = self.get_pair(pair_names)
        hit = attacker.hit()
        protected = not both_attack
        defender.receive_hit(hit, protected)

        if not defender.is_alive():
            slain = defender.name

        return slain

    def get_pair(self, names):
        attacker = self.find_gladiator_by_name(names[0])
        defender = self.find_gladiator_by_name(names[1])    
        return attacker, defender

    def find_gladiator_by_name(self, name):
        numbers = range(len(self.gladiators))
        dict_of_gladiators = {self.gladiators[i].name:i for i in numbers}
        index = dict_of_gladiators[name]
        if len([index]):
            return self.gladiators[index]
        else:
            gladiator = None
            print(name, 'not found')
   
    def remove_gladiator(self, name):
        corpse = self.find_gladiator_by_name(name)
        if corpse:
            self.gladiators.remove(corpse)
        else:
            print('Body not found')

    def check_winner(self):
        winner = []           
        gladiators_left = len(self.gladiators)
        if gladiators_left == 1:
            winner = self.gladiators[0].name
        return winner

# Morituri
arena = Arena(name='Colosseum')
arena.add_gladiator(Gladiator('Spartacus'))
arena.add_gladiator(Gladiator('Ajax'))
arena.add_gladiator(Gladiator('Maximus'))
arena.add_gladiator(Gladiator('Achilles'))
arena.add_gladiator(Gladiator('Commodus'))

winner = arena.run_fight()
print(winner, 'wins')
