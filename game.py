from classes import *
from functions import *
from drop import *
from enemies import *

player = Player("Dmitry", 1, 100, 100, 10)
player_inventory = Player.Inventory(2, started_bag)

player_warehouse = Player.Warehouse(10)
player_armor = Player.PlayerArmor()
shop = Shop()

#player_inventory.inventory.append(started_bag)
player_inventory.inventory.append(iron_helmet)
#player_inventory.inventory.append(leather_helmet)
#player_warehouse.warehouse.append(apple)
#player_armor.armor["HELMET"] = leather_helmet
#player_armor.armor["CHEST"] = leather_chest

#fight(player, rat)
#fight(player, rat)

town_actions(player, player_inventory, shop, player_warehouse)

#dropped_items = drop_items(rat.level)

#drop_actions(player_inventory, dropped_items)

#player_armor.show_player_info(player)

#player_inventory.inventory_actions(player)

player_inventory.show_inventory()
#player_inventory.inventory_actions(player)
#player_inventory.equip_the_armor(player_inventory.inventory[1])
#bread.eat_the_food(player)
#print(player.health)

#player_inventory.equip_the_bag(player_inventory.inventory[0])

#player_inventory.inventory_actions()

#player_warehouse.warehouse_actions(player_inventory)
#shop_actions(player_inventory, shop)
#shop.show_goods()

#shop.buy_item_from_shop(1)
#player_inventory.show_inventory()

#shop.sell_item_to_shop(player_inventory.inventory[0])
#player_armor.show_player_info(player)
#player_inventory.show_inventory()