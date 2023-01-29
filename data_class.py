
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
    def add_data(self, name, value):
        self.data[name] = value
    def remove_data(self, name):
        self.data.pop(name, None)
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

