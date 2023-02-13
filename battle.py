import data_process

load_status = data_process.status.data

import random

class my_character:
    def __init__(self, name, my_status):
        self.name = name
        self.health = my_status['health']
        self.strength = my_status['strength']
        self.dexterity = my_status['dexterity']
        self.intelligence = my_status['intelligence']
        self.drunk = my_status['drunk']

    def attack(self, target):
        damage = self.strength * random.uniform(0.5, 1.5)
        target.health -= damage
        print(f"{self} attacked {target} for {damage:.2f} damage.")

class monster:
    def __init__(self, name, my_status):
        self.name = name
        self.health = my_status['health']
        self.strength = my_status['strength']
        self.dexterity = my_status['dexterity']
        self.intelligence = my_status['intelligence']
        self.exp = my_status['exp']

    def attack(self, target):
        damage = self.strength * random.uniform(0.5, 1.5)
        target.health -= damage
        print(f"{self} attacked {target} for {damage:.2f} damage.")

class Combat:
    def __init__(self, my_char, monsters):
        self.my_char = my_char
        self.monsters = monsters

    def simulate(self):
        ans = []
        for monster in self.monsters:
            while self.my_char.health > 0 and monster.health > 0:
                damage = self.my_char.strength
                monster.health -= damage
                ans += ["{} used normal attack and caused".format(self.my_char.name)]
                ans += ["{} damage.{}'s health is now {}".format(damage,monster.name, monster.health)]

                # monster attacks my_char
                damage = monster.strength
                self.my_char.health -= damage
                ans += ["Monster attacked my character and caused"] 
                ans += ["{} damage, {}s health is now {}".format(damage, self.my_char.name, self.my_char.health)]

            if self.my_char.health > 0:
                ans += ["My {} won the combat with this {}!".format(self.my_char.name,monster.name)]
            else:
                ans += ["Monster won the combat."]

        return ans

player = my_character("돌돌이", {'health': 100, 'strength': 10, 'dexterity': 10, 'intelligence': 10, 'drunk': False})
monsters = [monster("몬스터1", {'health': 75, 'strength': 8, 'dexterity': 8, 'intelligence': 8, 'exp': 10}),
            monster("몬스터2", {'health': 50, 'strength': 5, 'dexterity': 5, 'intelligence': 5, 'exp': 5})]


cc = Combat(player, monsters)
xx = cc.simulate()

for i in xx:
    print(i)