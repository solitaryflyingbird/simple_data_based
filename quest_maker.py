import json
import random
import os

class random_monster_pick:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        monsters_dict = self.json_to_dict(self.folder_path)
        pick = self.random_pick(monsters_dict)
        self.status = pick['status']
        self.monster_name = pick["name"]
        self.monster_num = random.randint(1,4)
        self.gold_reward = pick["status"]["rank"]*10 + (pick["status"]["rank"]*3 *self.monster_num)
        self.quest_name = "%s %d 마리 퇴치 \n보상 %d 골드" % (self.monster_name, self.monster_num, self.gold_reward)

    def json_to_dict(self, folder_path):
        result = {}
        for filename in os.listdir(folder_path):
            if filename.endswith('.json'):
                with open(os.path.join(folder_path, filename), 'r') as f:
                    result[filename[:-5]] = json.load(f)
        return result
    def random_pick(self, dictionary):
        x = random.choice(list(dictionary))
        return dictionary[x]


class quest_manager:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.quest1 = random_monster_pick(folder_path)
        self.quest2 = random_monster_pick(folder_path)

    def quest_load(self):
        self.quest1 = random_monster_pick(self.folder_path)
        self.quest2 = random_monster_pick(self.folder_path)

xx= quest_manager('./MONSTER/D')

