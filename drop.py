from classes import Food, Armor, Bag, Key, Weapon

'========================= Not for drop ======================'
old_key = Key("Old key", 15, "Old key: costs 15 gold, required to open founded chests")
'========================= Not for drop ======================'


"""" Here is a list of possible drops """

'========================= FOOD ======================'
apple = Food("apple", 1, 4, 5, "Apple: costs 4 gold, restores 5 health")
milk = Food("milk", 2, 6, 10, "Milk: costs 6 gold, restores 10 health")
bread = Food("bread", 3, 8, 15, "Bread: costs 8 gold, restores 15 health")
pie = Food("pie", 4, 10, 20, "Pie: costs 10 gold, restores 20 health")
soup = Food("soup", 5, 11, 25, "Soup: costs 11 gold, restores 25 health")
chicken = Food("chicken", 6, 13, 30, "Chicken: costs 13 gold, restores 30 health")

dropped_food = [bread, apple, milk, pie, soup, chicken]
'========================= HELMETS ======================'
straw_helmet = Armor("HELMET", "straw helmet", 1, 'common', 1, 6, "straw helmet: common quality, required level: 1, armor: 1, costs 6 gold")
leather_helmet = Armor("HELMET", "leather helmet", 2, 'common', 2, 11, "leather helmet: common quality, required level: 2, armor: 2, costs 11 gold")
iron_helmet = Armor("HELMET", "iron helmet", 4, 'common', 3, 16, "iron helmet: common quality, required level: 4, armor: 3, costs 16 gold")
steel_helmet = Armor("HELMET", "steel helmet", 6, 'rare', 4, 21, "steel helmet: rare quality, required level: 6, armor: 4, costs 21 gold")

dropped_helmets = [straw_helmet, leather_helmet, iron_helmet, steel_helmet]
'========================= CHESTS ======================'
straw_chest = Armor("CHEST", "straw chest", 1, 'common', 2, 8, "straw chest: common quality, required level: 1, armor: 2, costs 8 gold")
leather_chest = Armor("CHEST", "leather chest", 2, 'common', 3, 15, "leather chest: common quality, required level: 2, armor: 3, costs 15 gold")
iron_chest = Armor("CHEST", "iron chest", 4, 'common', 4, 22, "iron chest: common quality, required level: 4, armor: 4, costs 22 gold")
steel_chest = Armor("CHEST", "steel chest", 6, 'rare', 5, 29, "steel chest: rare quality, required level: 6, armor: 5, costs 29 gold")

dropped_chests = [straw_chest, leather_chest, iron_chest, steel_chest]
'========================= GLOVES ======================'
straw_gloves = Armor("GLOVES", "straw gloves", 1, 'common', 1, 5, "straw gloves: common quality, required level: 1, armor: 1, costs 5 gold")
leather_gloves = Armor("GLOVES", "leather gloves", 2, 'common', 2, 9, "leather gloves: common quality, required level: 2, armor: 2, costs 9 gold")
iron_gloves = Armor("GLOVES", "iron gloves", 4, 'common', 3, 13, "iron gloves: common quality, required level: 4, armor: 3, costs 13 gold")
steel_gloves = Armor("GLOVES", "steel gloves", 6, 'rare', 4, 17, "steel gloves: rare quality, required level: 6, armor: 4, costs 17 gold")

dropped_gloves = [straw_gloves, leather_gloves, iron_gloves, steel_gloves]
'========================= PANTS ======================'
straw_pants = Armor("PANTS", "straw pants", 1, 'common', 2, 7, "straw pants: common quality, required level: 1, armor: 2, costs 7 gold")
leather_pants = Armor("PANTS", "leather pants", 2, 'common', 3, 13, "leather pants: common quality, required level: 2, armor: 3, costs 13 gold")
iron_pants = Armor("PANTS", "iron pants", 4, 'common', 4, 19, "iron pants: common quality, required level: 4, armor: 4, costs 19 gold")
steel_pants = Armor("PANTS", "steel pants", 6, 'rare', 5, 25, "steel pants: rare quality, required level: 6, armor: 5, costs 25 gold")

dropped_pants = [straw_pants, leather_pants, iron_pants, steel_pants]
'========================= BOOTS ======================'
straw_boots = Armor("BOOTS", "straw boots", 1, 'common', 1, 6, "straw boots: common quality, required level: 1, armor: 1, costs 6 gold")
leather_boots = Armor("BOOTS", "leather boots", 2, 'common', 2, 11, "leather boots: common quality, required level: 2, armor: 2, costs 11 gold")
iron_boots = Armor("BOOTS", "iron boots", 4, 'common', 3, 16, "iron boots: common quality, required level: 4, armor: 3, costs 16 gold")
steel_boots = Armor("BOOTS", "steel boots", 6, 'rare', 4, 21, "steel boots: rare quality, required level: 6, armor: 4, costs 21 gold")

dropped_boots = [straw_boots, leather_boots, iron_boots, steel_boots]
'========================= BAGS ======================'
started_bag = Bag("poor bag", 1, 'common', 2, 8, "poor bag: common quality, capacity: 2, costs 8 gold")
linen_bag = Bag("linen bag", 1, 'common', 4, 13, "linen bag: common quality, capacity: 4, costs 13 gold")
cloth_bag = Bag("cloth bag", 3, 'common', 6, 23, "cloth bag: common quality, capacity: 6, costs 23 gold")
leather_bag = Bag("leather bag", 4, 'rare', 8, 33, "leather bag: common quality, capacity: 8, costs 33 gold")
silk_bag = Bag("silk bag", 6, 'rare', 10, 43, "silk bag: rare quality, capacity: 10, costs 43 gold")

dropped_bags = [linen_bag, cloth_bag, leather_bag, silk_bag]
'========================= Weapon ======================'
stick = Weapon("WEAPON", "Stick", 1, 'common', 1, 8, "A stick: poor quality, required level: 1, damage: 1, costs 8 gold")
sword = Weapon("WEAPON", "Sword", 2, 'common', 3, 17, "Sword: common quality, required level: 2, damage: 3, costs 17 gold")
long_sword = Weapon("WEAPON", "Long sword", 3, 'common', 4, 22, "Long sword: common quality, required level: 3, damage: 4, costs 22 gold")
axe = Weapon("WEAPON", "Axe", 4, 'common', 5, 27, "Axe: common quality, required level: 4, damage: 5, costs 27 gold")
broad_axe = Weapon("WEAPON", "Broad axe", 5, 'rare', 6, 32, "Broad axe: rare quality, required level: 5, damage: 6, costs 32 gold")
halberd = Weapon("WEAPON", "Halberd", 6, 'rare', 7, 37, "Halberd: rare quality, required level: 6, damage: 7, costs 37 gold")

dropped_weapons = [sword, long_sword, axe, broad_axe, halberd]
'========================= Weapon ======================'

list_of_all_items = [dropped_food, dropped_helmets, dropped_chests, dropped_gloves, dropped_pants, dropped_boots, dropped_bags, dropped_weapons]


def make_one_list_with_drop(list_of_all_items):
    all_items = []
    for category in list_of_all_items:
        for item in category:
            all_items.append(item)
    return all_items
