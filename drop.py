from classes import Food, Armor, Bag

"""" Here is a list of possible drops """

'========================= FOOD ======================'
bread = Food("bread", 3, 10, "bread: costs 3 gold, restores 10 health")
apple = Food("apple", 2, 5, "apple: costs 2 gold, restores 5 health")
milk = Food("milk", 4, 15, "milk: costs 4 gold, restores 15 health")

dropped_food = [bread, apple, milk]
'========================= HELMETS ======================'
leather_helmet = Armor("HELMET", "leather helmet", 1, 'common', 1, 4, "leather helmet: common quality, required level: 1, armor: 1, costs 4 gold")

dropped_helmets = [leather_helmet]
'========================= CHESTS ======================'
leather_chest = Armor("CHEST", "leather chest", 1, 'common', 2, 6, "leather chest: common quality, required level: 1, armor: 2, costs 6 gold")

dropped_chests = [leather_chest]
'========================= GLOVES ======================'
leather_gloves = Armor("GLOVES", "leather gloves", 1, 'common', 1, 3, "leather gloves: common quality, required level: 1, armor: 1, costs 3 gold")

dropped_gloves = [leather_gloves]
'========================= PANTS ======================'
leather_pants = Armor("PANTS", "leather pants", 1, 'common', 2, 5, "leather pants: common quality, required level: 1, armor: 2, costs 5 gold")

dropped_pants = [leather_pants]
'========================= BOOTS ======================'
leather_boots = Armor("BOOTS", "leather boots", 1, 'common', 1, 4, "leather boots: common quality, required level: 1, armor: 1, costs 4 gold")

dropped_boots = [leather_boots]
'========================= BAGS ======================'
started_bag = Bag("poor bag", 'common', 2, 5, "poor bag: common quality, capacity: 2, costs 5 gold")
linen_bag = Bag("linen bag", 'common', 4, 10, "linen bag: common quality, capacity: 3, costs 10 gold")

dropped_bags = [linen_bag]
'========================= BAGS ======================'

list_of_all_items = [dropped_food, dropped_helmets, dropped_chests, dropped_gloves, dropped_boots, dropped_bags]


def make_one_list_with_drop(list_of_all_items):
    all_items = []
    for category in list_of_all_items:
        for item in category:
            all_items.append(item)
    return all_items
