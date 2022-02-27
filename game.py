from classes import *
from functions import *
from drop import *

player = Player("Dmitry", 1, 100, 10)
player_inventory = Player.Inventory(3)

rat = Enemy("Rat", 3, 50, 50, 5)
#player_inventory.inventory.update({1: bread})
fight(player, rat)

dropped_items = drop_items(dropped_food, rat.level)

drop_actions(player_inventory, dropped_items)

player_inventory.show_inventory()

#player_inventory.inventory_actions()

#player_inventory.show_inventory()