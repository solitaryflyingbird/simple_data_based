import varible_data_class
import npc_class

import os
import json

status = varible_data_class.Status()
location = varible_data_class.Location()
inventory = varible_data_class.Inventory()
quest_progress = varible_data_class.QuestProgress()
gold = varible_data_class.GOLD()
gold.gold = 20
day = varible_data_class.DAY()
name = varible_data_class.NAME()

DATA = {"status" : status, "location" : location, "inventory" : inventory, "quest_progress" : quest_progress, "gold" : gold ,"name" : name, "day" : day}

NPC_DATA  = {}
ITEM_DATA = {}

def save_data(filename, data = DATA):
    with open(filename, "w") as file:
        json.dump({key: value.save() for key, value in data.items()}, file, indent = 4)


def load_data(filename):
    with open(filename, "r") as file:
        loaded_data = json.load(file)
        for key, value in loaded_data.items():
            DATA[key].load(value)
    return DATA


def load_npcs(folder_name):
    for filename in os.listdir(folder_name):
        if filename.endswith('.json'):
            with open(os.path.join(folder_name, filename), "r") as file:
                print(filename)
                npc_data = json.load(file)
                NPC_DATA[npc_data["name"]] = npc_data
def load_items(folder_name):
    for filename in os.listdir(folder_name):
        if filename.endswith('.json'):
            with open(os.path.join(folder_name, filename), "r") as file:
                item_data = json.load(file)
                ITEM_DATA[item_data["name"]] = item_data


load_npcs("NPC")
load_items("ITEM")


##테스트 코드
x = ITEM_DATA["item1"]

inventory.add_item(ITEM_DATA["item1"]["name"], 1)

inventory.add_item(ITEM_DATA["item1"], 2)

inventory.remove_item("item1", 1)
inventory.remove_item(ITEM_DATA["item1"]["name"], 1)

print(DATA["inventory"].data)

