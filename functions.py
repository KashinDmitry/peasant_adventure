import random
from time import sleep
from drop import *
from classes import Player
from classes import Shop
from enemies import *


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


def drop_actions(player_inventory, drop, player):
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
            if len(Player.Inventory.inventory) == player_inventory.inventory_size:
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
            Player.Inventory.inventory_actions(player_inventory, player)
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
                    print(
                        f'You are going to sell {Player.Inventory.inventory[item_index - 1].name} for {Player.Inventory.inventory[item_index - 1].price // 2} gold, are you sure? y/n')
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


def town_actions(player, player_inventory, shop, warehouse, player_armor):
    while True:
        if player.health > 0:
            action = ''
            print(
                "Choose action: 1 - go to outside, 2- open inventory, 3 - show player info, 4 - visit warehouse, 5 - visit shop, 6 - restore full health in hospital, 7 - end the game")
            try:
                action = int(input())
            except ValueError:
                print("Incorrect input. Please enter a number")
            if action == 1:
                explore_the_world(player, player_inventory)
            elif action == 2:
                Player.Inventory.inventory_actions(player_inventory, player)
            elif action == 3:
                player_armor.show_player_info(player)
                continue
            elif action == 4:
                warehouse.warehouse_actions(player_inventory)
                continue
            elif action == 5:
                shop_actions(player_inventory, shop)
            elif action == 6:
                player.restore_full_health()
                print(f"Health has been restored. Player health is {player.health}")
                continue
            elif action == 7:
                print(f'Are you sure you want to end the game? y/n')
                answer = str(input())
                if answer == 'y':
                    print('Thanks for the game!')
                    break
                elif answer == 'n':
                    continue
                else:
                    print("Incorrect input. Please enter 'y' or 'n'")
            else:
                continue
        else:
            print('Thanks for the game!')
            break


def min_attack(base_attack):
    low_attack = base_attack * 1
    return low_attack


def max_attack(base_attack):
    hight_attack = base_attack * 1.5
    return hight_attack


def attack_type():
    chance = random.randint(1, 100)
    if chance <= 10:
        return 'miss'
    elif 10 < chance <= 89:
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
            attack_scale = attack_type()
            if attack_scale == "miss":
                print('{yellow}Вы промахнулись{endcolor}'.format(yellow='\033[93m', endcolor='\033[0m'))
                player_strike = 0
            elif attack_scale == "critical":
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
            attack_scale = attack_type()
            if attack_scale == "miss":
                print('{yellow}Противник промахнулся{endcolor}'.format(yellow='\033[93m', endcolor='\033[0m'))
                enemy_strike = 0
            elif attack_scale == "critical":
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
        print("================= Fight has ended =================")
        player.get_exp(enemy)
        drop_from_enemy = drop_items(enemy.level)
        drop_gold(player.Inventory, enemy)
        enemy.restore_full_health()
        player_is_dead = False
        return player_is_dead, drop_from_enemy
    else:
        print("{red}YOU DIED...{endcolor}".format(red='\033[91m', endcolor='\033[0m'))
        sleep(3)
        drop = []
        player_is_dead = True
        return player_is_dead, drop


def choose_action_in_open_world():
    action_chance = random.randint(1, 100)
    if action_chance <= 47:
        return 'travel'
    elif 47 < action_chance <= 94:
        return 'attack'
    else:
        return 'find chest'


def choose_enemies_to_fight(enemies_scale):
    enemies = []
    try:
        for enemy in all_enemies[enemies_scale]:
            enemies.append(enemy)
        for enemy in all_enemies[enemies_scale + 1]:
            enemies.append(enemy)
    except KeyError:
        for enemy in all_enemies[len(all_enemies)]:
            enemies.append(enemy)
    return enemies


def open_chest(loot_scale, player_inventory, player):
    if player_inventory.inventory.count(old_key) == 0:
        print("You don't have a key to open the chest")
    else:
        gold_in_the_chest = 7 * loot_scale
        player_inventory.inventory_gold += gold_in_the_chest
        print(f"You have found {gold_in_the_chest} gold")
        key_index = player_inventory.inventory.index(old_key)
        player_inventory.remove_item_from_inventory(key_index + 1)
        drop = drop_items(loot_scale)
        drop_actions(player_inventory, drop, player)


def explore_the_world(player, player_inventory):
    direction = ['north', 'south', 'forest', 'river', 'west', 'east', 'fields']
    actions = []
    enemies_scale_counter = 0
    enemies_list = {}
    k = 2
    while True:
        enemies_scale = 1 + enemies_scale_counter // 5
        if k % 2 == 0:
            for count, event in enumerate(range(3), start=1):
                actions.append(choose_action_in_open_world())
                enemies = choose_enemies_to_fight(enemies_scale)
                chosen_enemy = random.choice(enemies)
                enemies_list[count] = chosen_enemy
            k += 1
        else:
            for count, i in enumerate(actions, start=1):
                if i == 'travel':
                    print(f'{count}: Travel to {random.choice(direction)}')
                elif i == 'attack':
                    print(f'{count}: Attack {enemies_list[count].name} (level {enemies_list[count].level})')
                else:
                    print(f'{count}: Explore the hidden chest!')
            print("Choose action (1, 2, 3...) or 4 - return to town")
            try:
                action = int(input())
                if action == 1 or action == 2 or action == 3:
                    if actions[action-1] == 'travel':
                        print(f"You are traveling...")
                        enemies_scale_counter += 1
                        actions.clear()
                        enemies_list.clear()
                        k += 1
                    elif actions[action-1] == 'attack':
                        print(f"you are fighting {enemies_list[action].name}")
                        player_is_dead, dropped_items = fight(player, enemies_list[action])
                        if not player_is_dead:
                            drop_actions(player_inventory, dropped_items, player)
                            actions.clear()
                            enemies_list.clear()
                            k += 1
                            print("Continue adventure...")
                        else:
                            break
                    else:
                        print("You are going to open the chest!")
                        open_chest(enemies_scale, player_inventory, player)
                        print("Continue adventure...")
                        actions.clear()
                        enemies_list.clear()
                        k += 1
                elif action == 4:
                    print("Returning to town")
                    actions.clear()
                    enemies_list.clear()
                    break
                else:
                    print("Incorrect input. Please choose number from list")
            except ValueError:
                print("Incorrect input. Please enter a number")
            except IndexError:
                print("You have chosen item out of list. Please choose correct number")
