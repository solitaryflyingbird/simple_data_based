import json
#Status
#Location
#Inventory
#QuestProgress

class Name():
    def __init__(self, name = None):
        self.name = name.copy() if name is not None else "들실장"

class Status():
    def __init__(self):
        self.data = {
            "level": 1,
            "exp": 0,
            "health": 300,
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "drunk" : 0
        }
        self.skill_data=[ {
                "name" : "달빛배기",
                "damage_up" : 'intelligence',
                "chance" : 20
            }
        ]

    def status_update(self, attribute: str, value: int):
        self.data[attribute] += value
        if attribute == "exp":
            while self.data["exp"] >= (self.data["level"] ** 2) * 10:
                self.data["exp"] -= (self.data["level"] ** 2) * 10
                self.data["level"] += 1
                print(f"Congratulations, you have reached level {self.data['level']}!")
    def save(self):
        return self.data
    def load(self, load_data):
        self.data = load_data
class Location():
    def __init__(self):
        self.data = {
            "x": 0,
            "y": 0
            }
    def save(self):
        return self.data
    def load(self, load_data):
        self.data = load_data
class Inventory():
    def __init__(self):
        self.data = {}
    def add_item(self, item, quantity=1):
        try:
            item_name = item["name"]
        except:
            item_name = item
        if item_name in self.data:
            self.data[item_name] += quantity
        else:
            self.data[item_name] = quantity
    def remove_item(self, item, quantity=1):
        try:
            item_name = item["name"]
        except:
            item_name = item
        if item_name in self.data:
            self.data[item_name] -= quantity
            if self.data[item_name] <= 0:
                self.data.pop(item_name)
    def save(self):
        return self.data
    def load(self, load_data):
        self.data = load_data

class QuestProgress():
    def __init__(self):
        self.data = {}
    def add_data(self, name, value):
        self.data[name] = value
    def remove_data(self, name):
        self.data.pop(name, None)
    def save(self):
        return self.data
    def load(self, load_data):
        self.data = load_data

class NPC:
    def __init__(self, npc_data_file=None):
        if npc_data_file:
            with open(npc_data_file, "r") as file:
                npc_data = json.load(file)
                self.name = npc_data["name"]
                self.portrait = npc_data["portrait"]
                self.status = npc_data["status"]
                self.dialogue = npc_data["dialogue"]
        else:
            self.name = ""
            self.portrait = ""
            self.status = {}
            self.dialogue = {}
        
    def save(self, npc_data_file):
        with open(npc_data_file, "w") as file:
            json.dump({
                "name": self.name,
                "portrait": self.portrait,
                "status": self.status,
                "dialogue": self.dialogue
            }, file, indent=4)
class GOLD:
    def __init__(self, gold = 0):
        self.gold=0
class DAY:
    def __init__(self, gold = 0):
        self.day=1

"""
i = Inventory()
i.add_item("x",1)
i.add_item({"name" : "x"} , 1)

print(i.data)
"""