from classes import Food, Armor, Bag, Key, Weapon

'========================= Not for drop ======================'
old_key = Key("Old key", 15, "Old key: costs 15 gold, required to open founded chests")
'========================= Not for drop ======================'


"""" Here is a list of possible drops """

'========================= FOOD ======================'
apple = Food("apple", 1, 2, 5, "Apple: costs 2 gold, restores 5 health")
milk = Food("milk", 2, 4, 10, "Milk: costs 4 gold, restores 10 health")
bread = Food("bread", 3, 6, 15, "Bread: costs 6 gold, restores 15 health")
pie = Food("pie", 4, 8, 20, "Pie: costs 8 gold, restores 20 health")
soup = Food("soup", 5, 9, 25, "Soup: costs 9 gold, restores 25 health")
chicken = Food("chicken", 6, 11, 30, "Chicken: costs 11 gold, restores 30 health")

dropped_food = [bread, apple, milk, pie, soup, chicken]
'========================= HELMETS ======================'
straw_helmet = Armor("HELMET", "straw helmet", 1, 'common', 1, 4, "straw helmet: common quality, required level: 1, armor: 1, costs 4 gold")
leather_helmet = Armor("HELMET", "leather helmet", 2, 'common', 2, 9, "leather helmet: common quality, required level: 2, armor: 2, costs 9 gold")
iron_helmet = Armor("HELMET", "iron helmet", 4, 'common', 3, 14, "iron helmet: common quality, required level: 4, armor: 3, costs 14 gold")
steel_helmet = Armor("HELMET", "steel helmet", 6, 'rare', 4, 19, "steel helmet: rare quality, required level: 6, armor: 4, costs 19 gold")

dropped_helmets = [straw_helmet, leather_helmet, iron_helmet, steel_helmet]
'========================= CHESTS ======================'
straw_chest = Armor("CHEST", "straw chest", 1, 'common', 2, 6, "straw chest: common quality, required level: 1, armor: 2, costs 6 gold")
leather_chest = Armor("CHEST", "leather chest", 2, 'common', 3, 13, "leather chest: common quality, required level: 2, armor: 3, costs 13 gold")
iron_chest = Armor("CHEST", "iron chest", 4, 'common', 4, 20, "iron chest: common quality, required level: 4, armor: 4, costs 20 gold")
steel_chest = Armor("CHEST", "steel chest", 6, 'rare', 5, 27, "steel chest: rare quality, required level: 6, armor: 5, costs 27 gold")

dropped_chests = [straw_chest, leather_chest, iron_chest, steel_chest]
'========================= GLOVES ======================'
straw_gloves = Armor("GLOVES", "straw gloves", 1, 'common', 1, 3, "straw gloves: common quality, required level: 1, armor: 1, costs 3 gold")
leather_gloves = Armor("GLOVES", "leather gloves", 2, 'common', 2, 7, "leather gloves: common quality, required level: 2, armor: 2, costs 7 gold")
iron_gloves = Armor("GLOVES", "iron gloves", 4, 'common', 3, 11, "iron gloves: common quality, required level: 4, armor: 3, costs 11 gold")
steel_gloves = Armor("GLOVES", "steel gloves", 6, 'rare', 4, 15, "steel gloves: rare quality, required level: 6, armor: 4, costs 15 gold")

dropped_gloves = [straw_gloves, leather_gloves, iron_gloves, steel_gloves]
'========================= PANTS ======================'
straw_pants = Armor("PANTS", "straw pants", 1, 'common', 2, 5, "straw pants: common quality, required level: 1, armor: 2, costs 5 gold")
leather_pants = Armor("PANTS", "leather pants", 2, 'common', 3, 11, "leather pants: common quality, required level: 2, armor: 3, costs 11 gold")
iron_pants = Armor("PANTS", "iron pants", 4, 'common', 4, 17, "iron pants: common quality, required level: 4, armor: 4, costs 17 gold")
steel_pants = Armor("PANTS", "steel pants", 6, 'rare', 5, 23, "steel pants: rare quality, required level: 6, armor: 5, costs 23 gold")

dropped_pants = [straw_pants, leather_pants, iron_pants, steel_pants]
'========================= BOOTS ======================'
straw_boots = Armor("BOOTS", "straw boots", 1, 'common', 1, 4, "straw boots: common quality, required level: 1, armor: 1, costs 4 gold")
leather_boots = Armor("BOOTS", "leather boots", 2, 'common', 2, 9, "leather boots: common quality, required level: 2, armor: 2, costs 9 gold")
iron_boots = Armor("BOOTS", "iron boots", 4, 'common', 3, 14, "iron boots: common quality, required level: 4, armor: 3, costs 14 gold")
steel_boots = Armor("BOOTS", "steel boots", 6, 'rare', 4, 29, "steel boots: rare quality, required level: 6, armor: 4, costs 19 gold")

dropped_boots = [straw_boots, leather_boots, iron_boots, steel_boots]
'========================= BAGS ======================'
started_bag = Bag("poor bag", 1, 'common', 2, 5, "poor bag: common quality, capacity: 2, costs 5 gold")
linen_bag = Bag("linen bag", 1, 'common', 4, 10, "linen bag: common quality, capacity: 4, costs 10 gold")
cloth_bag = Bag("cloth bag", 3, 'common', 6, 20, "cloth bag: common quality, capacity: 6, costs 20 gold")
leather_bag = Bag("leather bag", 4, 'rare', 8, 30, "leather bag: common quality, capacity: 8, costs 30 gold")
silk_bag = Bag("silk bag", 6, 'rare', 10, 40, "silk bag: rare quality, capacity: 10, costs 40 gold")

dropped_bags = [linen_bag, cloth_bag, leather_bag, silk_bag]
'========================= Weapon ======================'
started_sword = Weapon("WEAPON", "Rusted sword", 1, 'common', 1, 5, "Rusted sword: common quality, required level: 1, damage: 1, costs 5 gold")
sword = Weapon("WEAPON", "Sword", 2, 'common', 3, 14, "Sword: common quality, required level: 2, damage: 3, costs 14 gold")
long_sword = Weapon("WEAPON", "Long sword", 3, 'common', 4, 19, "Sword: common quality, required level: 3, damage: 4, costs 19 gold")
axe = Weapon("WEAPON", "Axe", 4, 'common', 5, 24, "Axe: common quality, required level: 4, damage: 5, costs 24 gold")
broad_axe = Weapon("WEAPON", "Broad axe", 5, 'rare', 6, 29, "Sword: common quality, required level: 5, damage: 6, costs 29 gold")
halberd = Weapon("WEAPON", "Halberd", 6, 'rare', 7, 34, "Sword: common quality, required level: 6, damage: 7, costs 34 gold")

dropped_weapons = [sword, long_sword, axe, broad_axe, halberd]
'========================= Weapon ======================'

list_of_all_items = [dropped_food, dropped_helmets, dropped_chests, dropped_gloves, dropped_boots, dropped_bags, dropped_weapons]


def make_one_list_with_drop(list_of_all_items):
    all_items = []
    for category in list_of_all_items:
        for item in category:
            all_items.append(item)
    return all_items
