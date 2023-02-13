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

class monster:
    def __init__(self, name, my_status):
        self.name = name
        self.health = my_status['health']
        self.strength = my_status['strength']
        self.dexterity = my_status['dexterity']
        self.intelligence = my_status['intelligence']
        self.exp = my_status['exp']


class Combat:
    def __init__(self, my_char, monsters):
        self.my_char = my_char
        self.monsters = monsters

    def simulate(self):
        ans = []
        while self.my_char.health > 0 and any(monster.health > 0 for monster in self.monsters):
            for monster in self.monsters:
                if monster.health <= 0:
                    continue
                damage = monster.strength
                self.my_char.health -= damage
                ans += ["{} attacked {} and caused {} damage. {}'s health is now {}".format(
                    monster.name, self.my_char.name, damage, self.my_char.name, self.my_char.health
                )]

            # my_char attacks a random monster
            alive_monsters = [monster for monster in self.monsters if monster.health > 0]
            if alive_monsters:
                target = random.choice(alive_monsters)
                damage = self.my_char.strength
                target.health -= damage
                ans += ["{} used normal attack and caused {} damage to {}. {}'s health is now {}".format(
                    self.my_char.name, damage, target.name, target.name, target.health
                )]
                if target.health<=0:
                    ans+=["{} 은 쓰러졌다.".format(target.name)]

        if self.my_char.health > 0:
            ans += ["My {} won the combat!".format(self.my_char.name)]
        else:
            ans += ["Monster(s) won the combat."]

        return ans


player = my_character("돌돌이", {'health': 100, 'strength': 12, 'dexterity': 10, 'intelligence': 10, 'drunk': False})
monsters = [monster("몬스터1", {'health': 20, 'strength': 8, 'dexterity': 8, 'intelligence': 8, 'exp': 10}),
            monster("몬스터2", {'health': 50, 'strength': 5, 'dexterity': 5, 'intelligence': 5, 'exp': 5})]


cc = Combat(player, monsters)
xx = cc.simulate()

for i in xx:
    print(i)