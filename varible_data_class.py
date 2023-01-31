import json
#Status
#Location
#Inventory
#QuestProgress
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Status(metaclass=Singleton):
    def __init__(self):
        self.data = {
            "level": 1,
            "exp": 0,
            "health": 100,
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
        }

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
class Location(metaclass=Singleton):
    def __init__(self):
        self.data = {
            "x": 0,
            "y": 0
            }
    def save(self):
        return self.data
    def load(self, load_data):
        self.data = load_data
class Inventory(metaclass=Singleton):
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
    def get_items(self):
        return self.data.keys()
    def save(self):
        return self.data
    def load(self, load_data):
        self.data = load_data

class QuestProgress(metaclass=Singleton):
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

"""
i = Inventory()
i.add_item("x",1)
i.add_item({"name" : "x"} , 1)

print(i.data)
"""