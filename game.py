from classes import *
from functions import *
from drop import *

player = Player("Dmitry", 1, 100, 10)
player_inventory = Player.Inventory(2)

rat = Enemy("Rat", 3, 50, 50, 5)

#fight(player, rat)

#dropped_items = drop_items(dropped_food, rat.level)

#drop_actions(player_inventory, dropped_items)

player_inventory.show_inventory()


'''TO DO LIST
когда нибудь добавить обработку эксепшенов на ввод неверных чисел
если инвентарь полон, а в дропе еще есть вещи, то нужно не выкидывать из дроп меню (done)
круто было бы показывать пустые слоты в инвентаре
если при таке алл нет места в инвентаре, то показать длину списка дропа и кол-во свободных слотов в инвентаре (done)
написать первые юнит тесты
'''
