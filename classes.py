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
            empty_slots_in_inventory = self.inventory_size - len(self.inventory)
            print("Inventory: [gold:", self.inventory_gold, "]", end=' ')
            print("[items: ", end='')
            for item in self.inventory:
                print(f'[{self.inventory[item].name}]', end='')
            for i in range(empty_slots_in_inventory):
                print('[ ]', end='')
            print(']')

        def remove_item(self, item_index):
            print("self.inventory: ", self.inventory)
            self.inventory.pop(item_index-1)

        def inventory_actions(self):
            while True:
                print("Choose action: 1 - show inventory, 2 - remove X-th item from inventory, 3 - close inventory menu")
                action = int(input())
                if action == 1:
                    self.show_inventory()
                    continue
                elif action == 2:
                    print("Choose item to remove (1, 2, 3...)")
                    item_index = int(input())
                    self.remove_item(item_index)
                    continue
                elif action == 3:
                    break


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
