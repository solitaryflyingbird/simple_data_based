import json


class Item:
    def __init__(self, item_data_file=None):
        if item_data_file:
            with open(item_data_file, "r") as file:
                item_data = json.load(file)
                self.name = item_data["name"]
                self.description = item_data["description"]
                self.value = item_data["value"]
                self.type = item_data["type"]
                self.use = item_data.get("use")
                self.wear = item_data.get("wear")
        else:
            self.name = ""
            self.description = ""
            self.value = 0
            self.type = ""
            self.use = None
            self.wear = None

    def save(self, item_data_file):
        with open(item_data_file, "w") as file:
            json.dump({
                "name": self.name,
                "description": self.description,
                "value": self.value,
                "type": self.type,
                "use": self.use,
                "wear": self.wear
            }, file, indent=4)

x = Item()
x.save("item1")