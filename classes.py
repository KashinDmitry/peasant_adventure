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
    exp_for_new_level = 0
    global_game_score = 0
    health_per_level = 20

    def get_exp(self, enemy):
        self.exp_for_new_level += enemy.level * 2
        if self.exp_for_new_level >= self.level * 10:
            self.exp_for_new_level = 0
            self.level += 1
            self.base_health += 20
            self.restore_full_health()
            print(f"You have reached level {self.level}! Health has been restored. Base health + {self.health_per_level}")
        else:
            print(f"Player exp: {self.exp_for_new_level}/{self.level * 10}")

    class Inventory:
        inventory = []
        inventory_gold = 0

        def __init__(self, inventory_size, bag):
            self.inventory_size = inventory_size
            self.bag = bag

        def show_inventory(self, player_armor):
            empty_slots_in_inventory = self.inventory_size - len(self.inventory)
            print(f"{self.bag.name} : [gold:", self.inventory_gold, "]", end=' ')
            print("[items: ", end='')
            for count, item in enumerate(self.inventory, start=1):
                print(f'[{count}.{item.name}]', end='')
            for i in range(empty_slots_in_inventory):
                print('[ ]', end='')
            print(']')
            for key in player_armor.armor_keys:
                if player_armor.armor[key] == '-':
                    print(f"{key}: -")
                else:
                    print(f"{key}: {player_armor.armor[key].name} -", "armor:", player_armor.armor[key].armor)
            print(f"Weapon: {player_armor.weapon.name} - damage: {player_armor.weapon.damage}")

        def remove_item_from_inventory(self, item_index):
            print(f"{self.inventory[item_index - 1].name} has been removed from inventory")
            self.inventory.pop(item_index - 1)

        def equip_the_bag(self, new_bag):
            if len(self.inventory) > new_bag.capacity:
                print(f"New bag have not enough capacity. Current inventory have {len(self.inventory)} items, new bag has {new_bag.capacity} slots")
            else:
                temp = self.bag
                self.inventory_size = new_bag.capacity
                self.bag = new_bag
                self.remove_item_from_inventory(self.inventory.index(new_bag)+1)
                self.inventory.append(temp)
                print(f"{new_bag.name} is equipped")

        def eat_the_food(self, food_item, player):
            if player.health == player.base_health:
                print("Player health is full. No need to restore it")
            else:
                player.restore_health(food_item.restore_health_amount)
                self.remove_item_from_inventory(self.inventory.index(food_item)+1)
                print(f"You ate {food_item.name}. Current health is {player.health}")

        def equip_the_armor(self, armor_item, player):
            if armor_item.level > player.level:
                print(f"Player level is too low to equip this armor. Need level {armor_item.level},"
                      f" current player level is {player.level}")
            else:
                if Player.PlayerArmor.armor[armor_item.armor_type] == '-':
                    Player.PlayerArmor.armor[armor_item.armor_type] = armor_item
                    print(f"You have equipped {armor_item.name}")
                    self.remove_item_from_inventory(self.inventory.index(armor_item)+1)
                else:
                    temp = Player.PlayerArmor.armor[armor_item.armor_type]
                    Player.PlayerArmor.armor[armor_item.armor_type] = armor_item
                    print(f"You have equipped {armor_item.name}")
                    self.remove_item_from_inventory(self.inventory.index(armor_item)+1)
                    self.inventory.append(temp)

        def equip_the_weapon(self, weapon_item, player):
            if weapon_item.level > player.level:
                print(f"Player level is too low to equip this weapon. Need level {weapon_item.level},"
                      f" current player level is {player.level}")
            else:
                temp = Player.PlayerArmor.weapon
                Player.PlayerArmor.weapon = weapon_item
                print(f"You have equipped {weapon_item.name}")
                self.remove_item_from_inventory(self.inventory.index(weapon_item)+1)
                self.inventory.append(temp)

        def inventory_actions(self, player, player_armor):
            self.show_inventory(player_armor)
            while True:
                action = ''
                print("Choose action: 1 - show inventory, 2 - use/equip X-th item, 3 - inspect X-th item, 4 - remove X-th item from inventory, 5 - close inventory menu")
                try:
                    action = int(input())
                except ValueError:
                    print("Incorrect input. Please enter a number")
                if action == 1:
                    self.show_inventory(player_armor)
                    continue
                elif action == 2:
                    print("Choose item to use/equip (1, 2, 3...)")
                    try:
                        item_index = int(input())
                        if type(self.inventory[item_index-1]) == Food:
                            self.eat_the_food(self.inventory[item_index - 1], player)
                        elif type(self.inventory[item_index-1]) == Bag:
                            self.equip_the_bag(self.inventory[item_index - 1])
                        elif type(self.inventory[item_index-1]) == Armor:
                            self.equip_the_armor(self.inventory[item_index - 1], player)
                        elif type(self.inventory[item_index-1]) == Weapon:
                            self.equip_the_weapon(self.inventory[item_index - 1], player)
                        else:
                            print("Unknown item type")
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
                    print("Choose item to inspect (1, 2, 3...)")
                    try:
                        item_index = int(input())
                        try:
                            print(self.inventory[item_index - 1].description)
                            continue
                        except IndexError:
                            print("You have chosen item out of list. Please choose correct item")
                    except ValueError:
                        print("Incorrect input. Please enter a number")
                    except TypeError:
                        print("Incorrect input. Please enter a number")
                elif action == 4:
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
                elif action == 5:
                    break
                else:
                    continue

    class Warehouse:
        warehouse = []

        def __init__(self, warehouse_size):
            self.warehouse_size = warehouse_size

        def show_warehouse(self):
            empty_slots_in_warehouse = self.warehouse_size - len(self.warehouse)
            print("[items in warehouse: ", end='')
            k = 1
            for item in self.warehouse:
                print(f'[{k}.{item.name}]', end='')
                k += 1
            for i in range(empty_slots_in_warehouse):
                print('[ ]', end='')
            print(']')

        def remove_item_from_warehouse(self, item_index):
            self.warehouse.pop(item_index - 1)

        def store_item_to_warehouse(self, player_inventory, player_armor):
            print("Choose item to put into warehouse (1, 2, 3...)")
            player_inventory.show_inventory(player_armor)
            try:
                item_index = int(input())
                if len(self.warehouse) < self.warehouse_size:
                    print(f"You have put {player_inventory.inventory[item_index-1].name} to warehouse")
                    self.warehouse.append(player_inventory.inventory[item_index-1])
                    player_inventory.remove_item_from_inventory(item_index)
                else:
                    print("Not enough space in warehouse")
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

        def warehouse_actions(self, player_inventory, player_armor):
            self.show_warehouse()
            while True:
                action = ''
                print(
                    "Choose action: 1 - show warehouse, 2 - store item from inventory to warehouse, 3 - take item from warehouse, 4 - remove X-th item from warehouse, 5 - exit warehouse")
                try:
                    action = int(input())
                except ValueError:
                    print("Incorrect input. Please enter a number")
                if action == 1:
                    self.show_warehouse()
                    continue
                elif action == 2:
                    self.store_item_to_warehouse(player_inventory, player_armor)
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
        weapon = '-'

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
            total_armor = self.calculate_total_armor()
            print("Name:", player.name)
            print(f"Level: {player.level} [Exp {player.exp_for_new_level}/{player.level * 10}]")
            print(f"Health: {player.health}/{player.base_health}")
            print(f"Total armor: {total_armor}")
            print("Global score (not final):", player.global_game_score)


class Food():
    def __init__(self, name, level, price, restore_health_amount, description):
        self.name = name
        self.level = level
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


class Weapon():
    def __init__(self, weapon_type, name, level, quality, damage, price, description):
        self.weapon_type = weapon_type
        self.name = name
        self.level = level
        self.quality = quality
        self.damage = damage
        self.price = price
        self.description = description


class Bag():
    def __init__(self, name, level, quality, capacity, price, description):
        self.name = name
        self.level = level
        self.quality = quality
        self.capacity = capacity
        self.price = price
        self.description = description


class Key():
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


from drop import *


class Shop():
    goods = make_one_list_with_drop(list_of_all_items)
    goods.append(old_key)

    def __init__(self):
        pass

    def show_goods(self):
        for count, item in enumerate(self.goods, start=1):
            print(f'{count}: {item.description}')

    def buy_item_from_shop(self, item_index, player_inventory):
        item_price = self.goods[item_index - 1].price
        if player_inventory.inventory_gold >= item_price:
            player_inventory.inventory.append(self.goods[item_index - 1])
            player_inventory.inventory_gold -= item_price
            print(f"You have bought {self.goods[item_index - 1].name}. Gold left: {player_inventory.inventory_gold}")
        else:
            print(f"Not enough gold. Player gold is {player_inventory.inventory_gold}")

    def sell_item_to_shop(self, player_inventory, item_index):
        item = player_inventory.inventory[item_index]
        player_inventory.inventory_gold += item.price//2
        player_inventory.inventory.remove(item)
