import data_process
import random

load_status = data_process.status.data
skill_data = data_process.status.skill_data

print(load_status)

class my_character:
    def __init__(self, name, my_status, skill_data = None):
        self.name = name
        self.health = my_status['health']
        self.strength = my_status['strength']
        self.dexterity = my_status['dexterity']
        self.intelligence = my_status['intelligence']
        self.drunk = my_status['drunk']
        self.skill_list = skill_data

class monster:
    def __init__(self, name, my_status, skill_data =None):
        self.name = name
        self.health = my_status['health']
        self.strength = my_status['strength']
        self.dexterity = my_status['dexterity']
        self.intelligence = my_status['intelligence']
        self.exp = my_status['exp']
        self.skill_list = skill_data


class Combat:
    def __init__(self, my_char, monsters):
        self.my_char = my_char
        self.monsters = monsters
    def battle_system(self, attacker, defender):
        skill_list = attacker.skill_list
        avoid_chance = min(5, attacker.dexterity - defender.dexterity + 5)
        if random.randint(1, 100) < avoid_chance:
            battle_log = "{}은(는) 공격을 피했다".format(defender.name)
            return 0, battle_log

        if skill_list:
            for skill in skill_list:
                if random.randint(1, 100) < skill['chance']:
                    damage = int((getattr(attacker, skill['damage_up'])/10+1)*attacker.strength)
                    battle_log = "{}은(는) {} 스킬을 사용했다. {}가 받은 데미지는 {}. {}의 남은 체력은 {}이다.".format(
                        attacker.name, skill['name'], defender.name, damage, defender.name, defender.health
                    )
                    return damage, battle_log

        damage = attacker.strength
        battle_log = "{}은(는) 공격했다. {}가 받은 데미지는 {}. {}의 남은 체력은 {}이다.".format(
            attacker.name, defender.name, damage, defender.name, defender.health
        )
        return damage, battle_log

        ###[{'name': '달빛배기', 'damage_up': 'intelligence', 'chance': 10}]

    def simulate(self):
        battle_log = []
        battle_result = 1
        while True:
            #monster_attack
            for monster in self.monsters:
                if monster.health <= 0:
                    continue
                damage, log = self.battle_system(monster, self.my_char)
                self.my_char.health -= damage
                battle_log.append(log)
                if self.my_char.health <= 0:
                    battle_log.append("{} 은(는) 쓰러졌다.".format(self.my_char.name))
            
            if self.my_char.health <= 0 or any(monster.health <= 0 for monster in self.monsters):
                break
            # my_char attacks a random monster
            alive_monsters = [monster for monster in self.monsters if monster.health > 0]
            if alive_monsters:
                target = random.choice(alive_monsters)
                damage, log = self.battle_system(self.my_char, target)
                target.health -= damage
                battle_log.append(log)
                if target.health <= 0:
                    battle_log.append("{} 은(는) 쓰러졌다.".format(target.name))
            if self.my_char.health <= 0 or any(monster.health <= 0 for monster in self.monsters):
                break

        if self.my_char.health > 0:
            battle_log.append("{} 은(는) 전투에서 이겼다!".format(self.my_char.name))
            battle_result = 1
        else:
            battle_log.append("{} 은(는) 전투에서 패배했다!".format(self.my_char.name))
            battle_result = 0

        return (battle_log, battle_result)


player = my_character("돌돌이", {'health': 100, 'strength': 12, 'dexterity': 10, 'intelligence': 15, 'drunk': 10}, skill_data)
monsters = [monster("몬스터1", {'health': 210, 'strength': 8, 'dexterity': 8, 'intelligence': 8, 'exp': 10}),
            monster("몬스터2", {'health': 50, 'strength': 5, 'dexterity': 5, 'intelligence': 5, 'exp': 5})]


cc = Combat(player, monsters)
xx = cc.simulate()

for i in xx[0]:
    print(i)
