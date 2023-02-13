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
    def calculate_damage(self, attacker, defender):
        return attacker.strength

    def simulate(self):
        battle_log = []
        battle_result = 1
        while self.my_char.health > 0 and any(monster.health > 0 for monster in self.monsters):
            #monster_attack
            for monster in self.monsters:
                if monster.health <= 0:
                    continue
                damage = self.calculate_damage(monster, self.my_char)
                self.my_char.health -= damage
                battle_log += ["{}은(는) 공격했다. {}가 받은 데미지는 {}. {}의 남은 체력은 {}이다.".format(
                    monster.name, self.my_char.name, damage, self.my_char.name, self.my_char.health
                )]
                if self.my_char.health<=0:
                    battle_log+=["{} 은(는) 쓰러졌다.".format(self.my_char.name)]
            
            if self.my_char.health <= 0 or any(monster.health <= 0 for monster in self.monsters):
                break
            # my_char attacks a random monster
            alive_monsters = [monster for monster in self.monsters if monster.health > 0]
            if alive_monsters:
                target = random.choice(alive_monsters)
                damage = self.calculate_damage(self.my_char, target)
                target.health -= damage
                battle_log += ["{}은(는) 공격했다 {}가 받은 데미지는 {}. {}의 남은 체력은 {}이다.".format(
                    self.my_char.name, target.name, damage,  target.name, target.health
                )]
                if target.health<=0:
                    battle_log+=["{} 은(는) 쓰러졌다.".format(target.name)]

        if self.my_char.health > 0:
            battle_log += ["{} 은(는) 전투에서 이겼다!".format(self.my_char.name)]
            battle_result = 1

        if self.my_char.health > 0:
            battle_log += ["{} 은(는) 전투에서 이겼다!".format(self.my_char.name)]
            battle_result = 1
        else:
            battle_log += ["{} 은(는) 전투에서 패배했다!".format(self.my_char.name)]
            battle_result = 0
        return (battle_log, battle_result)


player = my_character("돌돌이", {'health': 100, 'strength': 12, 'dexterity': 10, 'intelligence': 10, 'drunk': False})
monsters = [monster("몬스터1", {'health': 20, 'strength': 8, 'dexterity': 8, 'intelligence': 8, 'exp': 10}),
            monster("몬스터2", {'health': 50, 'strength': 5, 'dexterity': 5, 'intelligence': 5, 'exp': 5})]


cc = Combat(player, monsters)
xx = cc.simulate()

for i in xx[0]:
    print(i)