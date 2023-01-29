import data_class
import json
status = data_class.Status()
location = data_class.Location()
inventory = data_class.Inventory()
quest_progress = data_class.QuestProgress()

DATA = {"status" : status, "location" : location, "inventory" : inventory, "quest_progress" : quest_progress}

def save_data(filename, data = DATA):
    with open(filename, "w") as file:
        json.dump({key: value.save() for key, value in data.items()}, file)


def load_data(filename):
    with open(filename, "r") as file:
        loaded_data = json.load(file)
        for key, value in loaded_data.items():
            DATA[key].load(value)
    return DATA

DATA = load_data("ddd")
print(location.data)