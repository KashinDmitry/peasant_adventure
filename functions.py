import random
from drop import *
from classes import Player


def drop_items(items, amount):
    print(f"You have found {amount} item(s):")
    drop = []
    for i in range(amount):
        random_item = random.choice(items)
        print(i+1, random_item.name)
        drop.append(random_item)
    return drop


def show_items(items_list):
    for i in range(len(items_list)):
        print(i+1, items_list[i].name)


def take_item(player_inventory, item):
    inventory_as_dict = Player.Inventory.inventory
    if len(inventory_as_dict) < player_inventory.inventory_size:
        inventory_as_dict.update({len(inventory_as_dict): item})
    else:
        print("Inventory is full")


def remove_item_from_list(items_list, item):
    items_list.remove(item)
    return items_list


def inspect_item(drop):
    print("Choose item to inspect (1, 2, 3...)")
    item_index = int(input())
    print(drop[item_index-1].description)


def drop_actions(player_inventory, drop):
    while True:
        empty_slots_in_inventory = player_inventory.inventory_size - len(Player.Inventory.inventory)
        print("Choose action: 1 - take all, 2 - inspect X-th item, 3 - take X-th item, 4 - close drop menu")
        action = int(input())
        if action == 1:
            if len(drop) > empty_slots_in_inventory:
                print(f"Not enough space to take all items. Items in drop = {len(drop)}, empty slots in inventory = {empty_slots_in_inventory}")
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
            item_index = int(input())
            take_item(player_inventory, drop[item_index-1])
            if len(Player.Inventory.inventory) == player_inventory.inventory_size:  # возможно стоит реализовать покрасивее
                continue
            else:
                remove_item_from_list(drop, drop[item_index-1])
                print("Взяли вещь и удалили из дропа")
            if len(drop) == 0:
                print("Drop list is empty")
                break
            else:
                print("Item(s) left in your drop:")
                show_items(drop)
                continue
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
    while player.health > 0 and enemy.health > 0:
        if k % 2 == 0:
            player_strike = random.uniform(min_attack(player.base_attack), max_attack(player.base_attack))
            #print("Playes attack basic ", player_strike)
            if attack_type() == "miss":
                print('{yellow}Вы промахнулись{endcolor}'.format(yellow='\033[93m', endcolor='\033[0m'))
                player_strike = 0
            elif attack_type() == "critical":
                print('{red}КРИТИЧЕСКИЙ УДАР!{endcolor}'.format(red='\033[91m', endcolor='\033[0m'))
                player_strike = round(player_strike, 1) * 2
            else:
                player_strike = round(player_strike, 1)
            #           print("player_strike = ", player_strike)
            enemy.health = enemy.health - player_strike
            print(f"{player.name} deals {player_strike} damage")
            print(f"{enemy.name}'s health = ", round(enemy.health))
            k += 1
        else:
            enemy_strike = random.uniform(min_attack(enemy.base_attack), max_attack(enemy.base_attack))
            #print("Enemy attack basic ", enemy_strike)
            if attack_type() == "miss":
                print('{yellow}Противник промахнулся{endcolor}'.format(yellow='\033[93m', endcolor='\033[0m'))
                enemy_strike = 0
            elif attack_type() == "critical":
                print('{red}КРИТИЧЕСКИЙ УДАР!{endcolor}'.format(red='\033[91m', endcolor='\033[0m'))
                enemy_strike = round(enemy_strike, 1) * 2
            else:
                enemy_strike = round(enemy_strike, 1)
            player.health = player.health - enemy_strike
            print(f"{enemy.name} deals {enemy_strike} damage")
            print(f"{player.name}'s health = ", round(player.health))
            k += 1
    if enemy.health <= 0:
        print(f"{enemy.name} has been defeated")
        enemy.restore_full_health(enemy.base_health)
        print("================= Fight has ended =================")
    else:
        print("{red}YOU DIED...{endcolor}".format(red='\033[91m', endcolor='\033[0m'))