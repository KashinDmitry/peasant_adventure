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
            k = 1
            for item in self.inventory:
                print(f'[{k}.{item.name}]', end='')
                k += 1
            for i in range(empty_slots_in_inventory):
                print('[ ]', end='')
            print(']')

        def remove_item_from_inventory(self, item_index):
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
                        self.remove_item_from_inventory(item_index)
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

    class Warehouse:
        warehouse = []

        def __init__(self, warehouse_size):
            self.warehouse_size = warehouse_size

        def show_warehouse(self):
            empty_slots_in_warehouse = self.warehouse_size - len(self.warehouse)
            print("[items: ", end='')
            k = 1
            for item in self.warehouse:
                print(f'[{k}.{item.name}]', end='')
                k += 1
            for i in range(empty_slots_in_warehouse):
                print('[ ]', end='')
            print(']')

        def remove_item_from_warehouse(self, item_index):
            self.warehouse.pop(item_index - 1)

        def store_item_to_warehouse(self, player_inventory):
            print("Choose item to put into warehouse (1, 2, 3...)")
            player_inventory.show_inventory()
            try:
                item_index = int(input())
                if len(self.warehouse) < self.warehouse_size:
                    print(f"You have put {player_inventory.inventory[item_index-1].name} to warehouse")
                    self.warehouse.append(player_inventory.inventory[item_index-1])
                    player_inventory.remove_item_from_inventory(item_index)
                else:
                    print("Not enough slots in warehouse")
            except ValueError:
                print("ValueError Incorrect input. Please enter a number")
            except TypeError:
                print("TypeError Incorrect input. Please enter a number")
            except IndexError:
                print("You have chosen item out of list. Please choose correct item")

        def take_item_from_warehouse(self, player_inventory):
            self.show_warehouse()
            print("Choose item to take from warehouse (1, 2, 3...)")
            try:
                item_index = int(input())
                inventory_as_list = Player.Inventory.inventory
                if len(inventory_as_list) < player_inventory.inventory_size:
                    inventory_as_list.append(self.warehouse[item_index-1])
                    print(f"You have taken {self.warehouse[item_index-1].name} from warehouse")
                    self.warehouse.pop(item_index - 1)
                else:
                    print("Inventory is full")
            except ValueError:
                print("ValueError Incorrect input. Please enter a number")
            except TypeError:
                print("TypeError Incorrect input. Please enter a number")
            except IndexError:
                print("You have chosen item out of list. Please choose correct item")

        def warehouse_actions(self, player_inventory):
            while True:
                action = ''
                item_index = ''
                print(
                    "Choose action: 1 - show warehouse, 2 - store item from inventory to warehouse, 3 - take item from warehouse, 4 - remove X-th item from inventory, 5 - exit warehouse")
                try:
                    action = int(input())
                except ValueError:
                    print("Incorrect input. Please enter a number")
                if action == 1:
                    self.show_warehouse()
                    continue
                elif action == 2:
                    self.store_item_to_warehouse(player_inventory)
                    continue
                elif action == 3:
                    self.take_item_from_warehouse(player_inventory)
                    continue
                elif action == 4:
                    print("Choose item to remove (1, 2, 3...)")
                    try:
                        item_index = int(input())
                        self.remove_item_from_warehouse(item_index)
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
                elif action == 5:
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
