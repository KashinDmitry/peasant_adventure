from functions import *
from drop import *

print("Enter you name: ")
player_name = str(input())

player = Player(player_name, 1, 100, 100, 10)
player_inventory = Player.Inventory(2, started_bag)
player_warehouse = Player.Warehouse(10)
player_armor = Player.PlayerArmor()
Player.PlayerArmor.weapon = stick
shop = Shop()

print(f"Greetings {player_name}! Old org (level 7) terrorizes the village you live in. Your task is prepare to battle, find the old ogr and kill him!")

town_actions(player, player_inventory, shop, player_warehouse, player_armor)