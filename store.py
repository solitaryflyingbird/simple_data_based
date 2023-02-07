class Store:
    def __init__(self, inventory, gold):
        self.inventory = inventory
    def buy(self, item, quantity, price):
        self.inventory.add_item(item, quantity)
        if self.gold.gold >= price *quantity:
            self.gold.gold -= price *quantity
        else:
            print("don't have enough gold")
    def sell(self, item, quantity, price):
        self.inventory.remove_item(item, quantity)
        self.gold.gold += price *quantity

class Potion_Store:
    def __init__(self, gold):
        self.gold = gold
    def buy(self,price, gold):
        self.inventory.add_item(item, quantity)
        if self.gold.gold >= price *quantity:
            self.gold.gold -= price *quantity
        else:
            print("don't have enough gold")