import json

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


