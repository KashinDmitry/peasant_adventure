from classes import Unit

rat = Unit("Rat", 1, 20, 20, 3)
spider = Unit("Spider", 1, 25, 25, 4)
wolf = Unit("Wolf", 1, 30, 30, 8)
old_wolf = Unit("Old wolf", 1, 35, 35, 6)
kobolt = Unit("Kobolt", 1, 37, 37, 6)
first_level_enemies = [rat, spider, wolf, old_wolf, kobolt]

murloc = Unit("Murloc", 2, 40, 40, 8)
young_goblin = Unit("Young goblin", 2, 40, 40, 9)
goblin = Unit("Goblin", 2, 45, 45, 9)
harpy = Unit("Harpy", 2, 47, 47, 10)
bear = Unit("Bear", 2, 55, 55, 11)
second_level_enemies = [murloc, young_goblin, goblin, harpy, bear]

nimp = Unit("Nimp", 3, 65, 65, 6)
bandit = Unit("Bandit", 3, 60, 60, 11)
skeleton = Unit("Skeleton", 3, 50, 50, 15)
ghost = Unit("Ghost", 3, 60, 60, 12)
skeleton_archer = Unit("Skeleton archer", 3, 50, 50, 16)
third_level_enemies = [nimp, bandit, skeleton, ghost, skeleton_archer]

shaman = Unit("Shaman", 4, 63, 63, 13)
corpse = Unit("Сorpse", 4, 65, 65, 13)
wrath = Unit("Wrath", 4, 55, 55, 17)
leper = Unit("Leper", 4, 68, 68, 15)
witch = Unit("Witch", 4, 62, 62, 16)
fourth_level_enemies = [shaman, corpse, wrath, leper, witch]

drowner = Unit("Drowner", 5, 70, 70, 16)
wyvern = Unit("Wyvern", 5, 72, 72, 17)
phantom = Unit("Phantom", 5, 75, 75, 17)
griffin = Unit("Griffin", 5, 79, 79, 18)
mimic = Unit("Mimic", 5, 85, 85, 20)
fifth_level_enemies = [drowner, wyvern, phantom, griffin, mimic]

berserk = Unit("Berserk", 6, 80, 80, 25)
reaper = Unit("Reaper", 6, 88, 88, 22)
jumper = Unit("Jumper", 6, 90, 90, 24)
night_hunter = Unit("Night hunter", 6, 95, 95, 25)
troll = Unit("Troll", 6, 100, 100, 27)
sixth_level_enemies = [berserk, reaper, jumper, night_hunter, troll]

old_leshy = Unit("Old leshy", 7, 150, 150, 35)
boss = [old_leshy]

all_enemies = {1: first_level_enemies,
               2: second_level_enemies,
               3: third_level_enemies,
               4: fourth_level_enemies,
               5: fifth_level_enemies,
               6: sixth_level_enemies,
               7: boss}
