from classes import Food, Armor, Bag, Key, Weapon

'========================= Not for drop ======================'
old_key = Key("Old key", 15, "Old key: costs 15 gold, required to open founded chests")
'========================= Not for drop ======================'


"""" Here is a list of possible drops """

'========================= FOOD ======================'
apple = Food("apple", 1, 2, 5, "apple: costs 2 gold, restores 5 health")
bread = Food("bread", 1,  3, 10, "bread: costs 3 gold, restores 10 health")
milk = Food("milk", 2, 4, 15, "milk: costs 4 gold, restores 15 health")

dropped_food = [bread, apple, milk]
'========================= HELMETS ======================'
leather_helmet = Armor("HELMET", "leather helmet", 1, 'common', 1, 4, "leather helmet: common quality, required level: 1, armor: 1, costs 4 gold")
iron_helmet = Armor("HELMET", "iron helmet", 2, 'common', 2, 9, "iron helmet: common quality, required level: 2, armor: 2, costs 9 gold")

dropped_helmets = [leather_helmet, iron_helmet]
'========================= CHESTS ======================'
leather_chest = Armor("CHEST", "leather chest", 1, 'common', 2, 6, "leather chest: common quality, required level: 1, armor: 2, costs 6 gold")
iron_chest = Armor("CHEST", "iron chest", 2, 'common', 3, 13, "iron chest: common quality, required level: 2, armor: 3, costs 13 gold")

dropped_chests = [leather_chest, iron_chest]
'========================= GLOVES ======================'
leather_gloves = Armor("GLOVES", "leather gloves", 1, 'common', 1, 3, "leather gloves: common quality, required level: 1, armor: 1, costs 3 gold")
iron_gloves = Armor("GLOVES", "iron gloves", 2, 'common', 2, 7, "iron gloves: common quality, required level: 2, armor: 2, costs 7 gold")

dropped_gloves = [leather_gloves, iron_gloves]
'========================= PANTS ======================'
leather_pants = Armor("PANTS", "leather pants", 1, 'common', 2, 5, "leather pants: common quality, required level: 1, armor: 2, costs 5 gold")
iron_pants = Armor("PANTS", "iron pants", 2, 'common', 3, 11, "leather pants: common quality, required level: 2, armor: 3, costs 11 gold")

dropped_pants = [leather_pants, iron_pants]
'========================= BOOTS ======================'
leather_boots = Armor("BOOTS", "leather boots", 1, 'common', 1, 4, "leather boots: common quality, required level: 1, armor: 1, costs 4 gold")
iron_boots = Armor("BOOTS", "iron boots", 2, 'common', 2, 9, "iron boots: common quality, required level: 2, armor: 2, costs 9 gold")

dropped_boots = [leather_boots, iron_boots]
'========================= BAGS ======================'
started_bag = Bag("poor bag", 1, 'common', 2, 5, "poor bag: common quality, capacity: 2, costs 5 gold")
linen_bag = Bag("linen bag", 1, 'common', 4, 10, "linen bag: common quality, capacity: 4, costs 10 gold")
silk_bag = Bag("silk bag", 2, 'rare', 6, 20, "silk bag: rare quality, capacity: 6, costs 20 gold")

dropped_bags = [linen_bag, silk_bag]
'========================= Weapon ======================'
started_sword = Weapon("WEAPON", "Rusted sword", 1, 'common', 1, 5, "Rusted sword: common quality, required level: 1, damage: 1, costs 5 gold")
sword = Weapon("WEAPON", "Sword", 1, 'common', 3, 14, "Sword: common quality, required level: 1, damage: 3, costs 14 gold")

dropped_weapons = [sword]
'========================= Weapon ======================'

list_of_all_items = [dropped_food, dropped_helmets, dropped_chests, dropped_gloves, dropped_boots, dropped_bags, dropped_weapons]


def make_one_list_with_drop(list_of_all_items):
    all_items = []
    for category in list_of_all_items:
        for item in category:
            all_items.append(item)
    return all_items
