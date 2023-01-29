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
    def save(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.data, file)

    def load(self, filename: str):
        with open(filename, "r") as file:
            self.data = json.load(file)

class Location(metaclass=Singleton):
    def __init__(self):
        self.x = 0
        self.y = 0
    def save(self):
        # code to save the location data to a file
        pass
    def load(self):
        # code to load the location data from a file
        pass

class Inventory(metaclass=Singleton):
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def save(self):
        # code to save the inventory data to a file
        pass
    def load(self):
        # code to load the inventory data from a file
        pass

class QuestProgress(metaclass=Singleton):
    def __init__(self):
        self.quests = []
    def add_quest(self, quest):
        self.quests.append(quest)
    def remove_quest(self, quest):
        self.quests.remove(quest)
    def save(self):
        # code to save the quest progress data to a file
        pass
    def load(self):
        # code to load the quest progress data from a file
        pass

