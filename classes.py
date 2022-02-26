class Unit:
    def __init__(self, name, level, health, base_attack):
        self.name = name
        self.level = level
        self.health = health
        self.base_attack = base_attack

    def restore_health(self, value):
        self.health += value


class Player(Unit):
    class Inventory:
        inventory = {}
        inventory_gold = 0

        def __init__(self, inventory_size):
            self.inventory_size = inventory_size

        def show_inventory(self):
            print("Inventory: [gold:", self.inventory_gold, "]", end=' ')
            print("[items: ", end='')
            for item in self.inventory:
                print(self.inventory[item].name, end=' ')
            print(']')


class Enemy(Unit):
    def __init__(self, name, level, base_health, health, base_attack):
        self.name = name
        self.level = level
        self.base_health = base_health
        self.health = health
        self.base_attack = base_attack

    def restore_full_health(self, base_health):
        self.health = base_health


class Food():
    def __init__(self, name, price, restore_health_amount, description):
        self.name = name
        self.price = price
        self.restore_health_amount = restore_health_amount
        self.description = description
