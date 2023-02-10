import json
import random
import os


def json_to_dict(folder_path):
    result = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            with open(os.path.join(folder_path, filename), 'r') as f:
                result[filename[:-5]] = json.load(f)
    return result
def random_pick(dictionary):
    x = random.choice(list(dictionary))
    return dictionary[x]

folder_path = './MONSTER/D'
monsters_dict = json_to_dict(folder_path)
pick = random_pick(monsters_dict)
monster_name = pick["name"]
monster_num = random.randint(1,4)
print(pick)
reward = pick["status"]["rank"]*10 + (pick["status"]["rank"]*3 *monster_num)

quest_name = "%s %d 마리 퇴치 \n보상 %d 골드" % (monster_name, monster_num, reward)


print(quest_name)