from classes import Unit

rat = Unit("Rat", 1, 20, 20, 4)
spider = Unit("Spider", 1, 25, 25, 5)
wolf = Unit("Wolf", 1, 30, 30, 9)
old_wolf = Unit("Old wolf", 1, 35, 35, 7)
kobolt = Unit("Kobolt", 1, 37, 37, 7)
first_level_enemies = [rat, spider, wolf, old_wolf, kobolt]

murloc = Unit("Murloc", 2, 40, 40, 9)
young_goblin = Unit("Young goblin", 2, 40, 40, 10)
goblin = Unit("Goblin", 2, 45, 45, 10)
harpy = Unit("Harpy", 2, 47, 47, 11)
bear = Unit("Bear", 2, 55, 55, 12)
second_level_enemies = [murloc, young_goblin, goblin, harpy, bear]

nimp = Unit("Nimp", 3, 65, 65, 10)
bandit = Unit("Bandit", 3, 60, 60, 12)
skeleton = Unit("Skeleton", 3, 50, 50, 16)
ghost = Unit("Ghost", 3, 60, 60, 13)
skeleton_archer = Unit("Skeleton archer", 3, 50, 50, 17)
third_level_enemies = [nimp, bandit, skeleton, ghost, skeleton_archer]

shaman = Unit("Shaman", 4, 63, 63, 14)
corpse = Unit("Сorpse", 4, 65, 65, 14)
wrath = Unit("Wrath", 4, 55, 55, 18)
leper = Unit("Leper", 4, 68, 68, 16)
witch = Unit("Witch", 4, 62, 62, 17)
fourth_level_enemies = [shaman, corpse, wrath, leper, witch]

drowner = Unit("Drowner", 5, 70, 70, 17)
wyvern = Unit("Wyvern", 5, 72, 72, 18)
phantom = Unit("Phantom", 5, 75, 75, 18)
griffin = Unit("Griffin", 5, 79, 79, 19)
mimic = Unit("Mimic", 5, 85, 85, 21)
fifth_level_enemies = [drowner, wyvern, phantom, griffin, mimic]

berserk = Unit("Berserk", 6, 80, 80, 26)
reaper = Unit("Reaper", 6, 88, 88, 23)
jumper = Unit("Jumper", 6, 90, 90, 25)
night_hunter = Unit("Night hunter", 6, 95, 95, 26)
troll = Unit("Troll", 6, 100, 100, 28)
sixth_level_enemies = [berserk, reaper, jumper, night_hunter, troll]

old_org = Unit("Old ogr - first stage boss", 7, 150, 150, 40)
boss_list = [old_org]

all_enemies = {1: first_level_enemies,
               2: second_level_enemies,
               3: third_level_enemies,
               4: fourth_level_enemies,
               5: fifth_level_enemies,
               6: sixth_level_enemies,
               7: boss_list}
