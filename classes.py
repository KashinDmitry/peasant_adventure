class Unit:
    def __init__(self, name, level, base_health, health, base_attack):
        self.name = name
        self.level = level
        self.health = health
        self.base_health = base_health
        self.base_attack = base_attack

    def restore_full_health(self):
        self.health = self.base_health

    def restore_health(self, value):
        if self.health + value >= self.base_health:
            self.restore_full_health()
        else:
            self.health += value


class Player(Unit):
    class Inventory:
        inventory = []
        inventory_gold = 0

        def __init__(self, inventory_size):
            self.inventory_size = inventory_size

        def show_inventory(self):
            empty_slots_in_inventory = self.inventory_size - len(self.inventory)
            print("Inventory: [gold:", self.inventory_gold, "]", end=' ')
            print("[items: ", end='')
            for item in self.inventory:
                print(f'[{item.name}]', end='')
            for i in range(empty_slots_in_inventory):
                print('[ ]', end='')
            print(']')

        def remove_item(self, item_index):
            self.inventory.pop(item_index - 1)

        def inventory_actions(self):
            while True:
                action = ''
                item_index = ''
                print(
                    "Choose action: 1 - show inventory, 2 - remove X-th item from inventory, 3 - close inventory menu")
                try:
                    action = int(input())
                except ValueError:
                    print("Incorrect input. Please enter a number")
                if action == 1:
                    self.show_inventory()
                    continue
                elif action == 2:
                    print("Choose item to remove (1, 2, 3...)")
                    try:
                        item_index = int(input())
                        self.remove_item(item_index)
                        continue
                    except ValueError:
                        print("Incorrect input. Please enter a number")
                        continue
                    except TypeError:
                        print("Incorrect input. Please enter a number")
                        continue
                    except IndexError:
                        print("You have chosen item out of list. Please choose correct item")
                        continue
                elif action == 3:
                    break
                else:
                    continue

    class PlayerArmor:
        armor = {'HELMET': '-',
                 'CHEST': '-',
                 'GLOVES': '-',
                 'PANTS': '-',
                 'BOOTS': '-'}

        armor_keys = armor.keys()

        def __init__(self):
            pass

        def calculate_total_armor(self):
            total_armor = 0
            for key in self.armor_keys:
                if self.armor[key] == '-':
                    continue
                else:
                    total_armor += self.armor[key].armor
            return total_armor

        def show_player_info(self, player):
            total_armor = 0
            print("Player level:", player.level)
            for key in self.armor_keys:
                if self.armor[key] == '-':
                    continue
                else:
                    print(f"{key}: {self.armor[key].name} -", "armor:", self.armor[key].armor)
                    total_armor += self.armor[key].armor
            print(f"Total armor: {total_armor}")


class Food():
    def __init__(self, name, price, restore_health_amount, description):
        self.name = name
        self.price = price
        self.restore_health_amount = restore_health_amount
        self.description = description


class Armor():
    def __init__(self, armor_type, name, level, quality, armor, price, description):
        self.armor_type = armor_type
        self.name = name
        self.level = level
        self.quality = quality
        self.armor = armor
        self.price = price
        self.description = description


from drop import *


class Shop():
    goods = make_one_list_with_drop(list_of_all_items)

    def __init__(self):
        pass

    def show_goods(self):
        for item in self.goods:
            print(f'{self.goods.index(item) + 1}: {item.description}')

    def buy_item_from_shop(self, item_index):
        player_gold = Player.Inventory.inventory_gold
        item_price = self.goods[item_index - 1].price
        if player_gold >= item_price:
            Player.Inventory.inventory.append(self.goods[item_index - 1])
            Player.Inventory.inventory_gold -= item_price
        else:
            print(f"Not enough gold. Player gold is {Player.Inventory.inventory_gold}")

    def sell_item_to_shop(self, item):
        Player.Inventory.inventory_gold += item.price//2
        Player.Inventory.inventory.remove(item)
