import varible_data_class
import non_varible_data_class
import json
status = varible_data_class.Status()
location = varible_data_class.Location()
inventory = varible_data_class.Inventory()
quest_progress = varible_data_class.QuestProgress()

DATA = {"status" : status, "location" : location, "inventory" : inventory, "quest_progress" : quest_progress}

def save_data(filename, data = DATA):
    with open(filename, "w") as file:
        json.dump({key: value.save() for key, value in data.items()}, file, indent = 4)


def load_data(filename):
    with open(filename, "r") as file:
        loaded_data = json.load(file)
        for key, value in loaded_data.items():
            DATA[key].load(value)
    return DATA

npc = non_varible_data_class.NPC("save_npc")
print(npc.status)
xxx = save_data("data_example")