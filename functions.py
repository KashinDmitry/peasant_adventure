import random
from drop import *
from classes import Player
from classes import Shop


def drop_items(amount):
    items_for_drop = make_one_list_with_drop(list_of_all_items)
    print(f"You have found {amount} item(s):")
    drop = []
    for i in range(amount):
        random_item = random.choice(items_for_drop)
        print(i + 1, random_item.name)
        drop.append(random_item)
    return drop


def drop_gold(player_inventory, defeated_enemy):
    dropped_gold = round(random.uniform(defeated_enemy.level, defeated_enemy.level + 2))
    player_inventory.inventory_gold += dropped_gold
    print(f"You have found {dropped_gold} gold")


def show_items(items_list):
    for i in range(len(items_list)):
        print(i + 1, items_list[i].name)


def take_item(player_inventory, item):
    inventory_as_list = Player.Inventory.inventory
    if len(inventory_as_list) < player_inventory.inventory_size:
        inventory_as_list.append(item)
    else:
        print("Inventory is full")


def remove_item_from_list(items_list, item):
    items_list.remove(item)
    return items_list


def inspect_item(drop):
    print("Choose item to inspect (1, 2, 3...)")
    try:
        item_index = int(input())
        try:
            print(drop[item_index - 1].description)
        except IndexError:
            print("You have chosen item out of list. Please choose correct item")
    except ValueError:
        print("Incorrect input. Please enter a number")
    except TypeError:
        print("Incorrect input. Please enter a number")


def drop_actions(player_inventory, drop):
    while True:
        action = ''
        item_index = ''
        empty_slots_in_inventory = player_inventory.inventory_size - len(Player.Inventory.inventory)
        print(
            "Choose action: 1 - take all, 2 - inspect X-th item, 3 - take X-th item, 4 - open inventory, 5 - close drop menu")
        try:
            action = int(input())
        except ValueError:
            print("Incorrect input. Please enter a number")
        if action == 1:
            if len(drop) > empty_slots_in_inventory:
                print(
                    f"Not enough space to take all items. Items in drop = {len(drop)}, empty slots in inventory = {empty_slots_in_inventory}")
                continue
            else:
                for item in drop:
                    take_item(player_inventory, item)
                break
        elif action == 2:
            inspect_item(drop)
            continue
        elif action == 3:
            print("Choose item to take (1, 2, 3...)")
            try:
                item_index = int(input())
            except ValueError:
                print("Incorrect input. Please enter a number")
                continue
            except TypeError:
                print("Incorrect input. Please enter a number")
                continue
            take_item(player_inventory, drop[item_index - 1])
            if len(
                    Player.Inventory.inventory) == player_inventory.inventory_size:  # возможно стоит реализовать покрасивее
                continue
            else:
                remove_item_from_list(drop, drop[item_index - 1])
            if len(drop) == 0:
                print("Drop list is empty")
                break
            else:
                print("Item(s) left in your drop:")
                show_items(drop)
                continue
        elif action == 4:
            Player.Inventory.inventory_actions(player_inventory)
            print("Item(s) left in your drop:")
            show_items(drop)
            continue
        elif action == 5:
            break
        else:
            continue


def shop_actions(player_inventory, shop_instance):
    while True:
        action = ''
        item_index = ''
        answer = ''
        print("Choose action: 1 - show goods, 2 - buy item, 3 - sell item, 4 - close shop menu")
        try:
            action = int(input())
        except ValueError:
            print("Incorrect input. Please enter a number")
        if action == 1:
            Shop.show_goods(shop_instance)
            continue
        elif action == 2:
            print(f'You have {Player.Inventory.inventory_gold} gold')
            print("Choose item to buy (1, 2, 3...)")
            try:
                item_index = int(input())
                Shop.buy_item_from_shop(shop_instance, item_index)
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
            Player.Inventory.show_inventory(player_inventory)
            print("Choose item from inventory (1, 2, 3...)")
            try:
                item_index = int(input())
                try:
                    print(f'You are going to sell {Player.Inventory.inventory[item_index - 1].name} for {Player.Inventory.inventory[item_index - 1].price//2} gold, are you sure? y/n')
                    answer = input()
                    if answer == 'y':
                        Shop.sell_item_to_shop(shop_instance, Player.Inventory.inventory[item_index - 1])
                        print('Item was sold')
                    else:
                        continue
                except IndexError:
                    print("You have chosen item out of list. Please choose correct item")
                    continue
            except ValueError:
                print("Incorrect input. Please enter a number")
            except TypeError:
                print("Incorrect input. Please enter a number")
        elif action == 4:
            break
        else:
            continue


def min_attack(base_attack):
    low_attack = base_attack * 0.5
    return low_attack


def max_attack(base_attack):
    hight_attack = base_attack * 1.5
    return hight_attack


def attack_type():
    chance = random.randint(1, 100)
    if chance <= 10:
        return 'miss'
    elif 10 < chance <= 79:
        return 'normal'
    else:
        return 'critical'


def fight(player, enemy):
    print("================= Fight is starting =================")
    k = 2
    player_armor = Player.PlayerArmor.calculate_total_armor(player.PlayerArmor)
    while player.health > 0 and enemy.health > 0:
        if k % 2 == 0:
            player_strike = random.uniform(min_attack(player.base_attack), max_attack(player.base_attack))
            if attack_type() == "miss":
                print('{yellow}Вы промахнулись{endcolor}'.format(yellow='\033[93m', endcolor='\033[0m'))
                player_strike = 0
            elif attack_type() == "critical":
                print('{red}КРИТИЧЕСКИЙ УДАР!{endcolor}'.format(red='\033[91m', endcolor='\033[0m'))
                player_strike = round(player_strike, 1) * 2
            else:
                player_strike = round(player_strike, 1)
            enemy.health = enemy.health - player_strike
            print(f"{player.name} deals {player_strike} damage")
            print(f"{enemy.name}'s health = ", round(enemy.health))
            k += 1
        else:
            enemy_strike = random.uniform(min_attack(enemy.base_attack), max_attack(enemy.base_attack))
            if attack_type() == "miss":
                print('{yellow}Противник промахнулся{endcolor}'.format(yellow='\033[93m', endcolor='\033[0m'))
                enemy_strike = 0
            elif attack_type() == "critical":
                print('{red}КРИТИЧЕСКИЙ УДАР!{endcolor}'.format(red='\033[91m', endcolor='\033[0m'))
                enemy_strike = round(enemy_strike, 1) * 2
            else:
                enemy_strike = round(enemy_strike, 1)
            print(f"{enemy.name} deals {enemy_strike} damage. {player_armor} damage were blocked by armor")
            if enemy_strike - player_armor <= 0:
                enemy_strike = 0
                print(f"{player.name}'s health = ", round(player.health))
                k += 1
            else:
                player.health = player.health - (enemy_strike - player_armor)
                print(f"{player.name}'s health = ", round(player.health))
                k += 1
    if enemy.health <= 0:
        print(f"{enemy.name} has been defeated!")
        drop_items(enemy.level)
        drop_gold(player.Inventory, enemy)
        enemy.restore_full_health()
        print("================= Fight has ended =================")
    else:
        print("{red}YOU DIED...{endcolor}".format(red='\033[91m', endcolor='\033[0m'))
