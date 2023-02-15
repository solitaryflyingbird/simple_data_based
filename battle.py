import data_process
import random



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
    def __init__(self, my_char, monsters, reward_gold):
        self.my_char = my_char
        self.monsters = monsters
        sum_exp_f = lambda list_of_instances: sum(item.exp for item in list_of_instances)
        self.reward_exp = sum_exp_f(monsters)
        self.reward_gold = reward_gold
        self.battle_result = None
    def battle_system(self, attacker, defender):
        skill_list = attacker.skill_list
        print(defender,defender.name, defender.dexterity, "d")
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
            if self.my_char.health <= 0 or all(monster.health <= 0 for monster in self.monsters):
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
            if self.my_char.health <= 0 or all(monster.health <= 0 for monster in self.monsters):
                break

        if self.my_char.health > 0:
            battle_log.append("{} 은(는) 전투에서 이겼다!".format(self.my_char.name))
            battle_result = 1
        else:
            battle_log.append("{} 은(는) 전투에서 패배했다!".format(self.my_char.name))
            battle_result = 0
        self.battle_result = battle_result
        return (battle_log, battle_result)

    def return_result(self):
        if self.battle_result == 1:
            return self.reward_gold, self.reward_exp
        if self.battle_result == 0:
            return "죽었다"
def make_monsters(name, status, num):
    monsters_arr = []
    for _ in range(num):
        monsters_arr.append(monster(name, status))
        print(monsters_arr[0].dexterity)
    return monsters_arr



"""
monsters_arr_test = [monster("몬스터1", {'health': 250, 'strength': 5, 'dexterity': 8, 'intelligence': 8, 'exp': 10}),
            monster("몬스터2", {'health': 50, 'strength': 5, 'dexterity': 5, 'intelligence': 5, 'exp': 5})]


player = my_character(data_process.name.name, data_process.status.data, data_process.status.skill_data)

ccc = Combat(player, monsters_arr_test, 10)
xx = ccc.simulate()

for i in xx[0]:
    print(i)

print(ccc.return_result())
"""