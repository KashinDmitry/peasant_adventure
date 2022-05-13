import unittest
from classes import *
from functions import *


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player = Player("Dmitry", 1, 100, 100, 10)
        self.player_inventory = Player.Inventory(2, started_bag)
        self.player_warehouse = Player.Warehouse(5)
        self.player_armor = Player.PlayerArmor()
        Player.PlayerArmor.weapon = stick
        self.shop = Shop()
        self.rat = Unit("Rat", 1, 50, 50, 5)

    def test_restore_health(self):
        self.player.health = 80
        self.player.restore_health(11)
        assert self.player.health == 91, f'wrong amount health was restored. Should be 91, not {self.player.health}'
        self.player.restore_health(10)
        assert self.player.health == 100, f'wrong amount health was restored. Should be 100, not {self.player.health}'

    def test_buy_item_from_shop(self):
        self.player_inventory.inventory_gold = 20
        bread_index = self.shop.goods.index(bread)
        self.shop.buy_item_from_shop(bread_index + 1, self.player_inventory)
        assert self.player_inventory.inventory_gold == 20 - bread.price, f'Wrong calculation. Gold left should be equal {20 - bread.price},' \
                                                                        f' not {self.player_inventory.inventory_gold}'
        assert self.player_inventory.inventory[0] == bread, f'Wrong bought item. Should be bread,' \
                                                            f'got {self.player_inventory.inventory[0].name} instead'

    def test_sell_item_to_shop(self):
        self.player_inventory.inventory_gold = 0
        self.player_inventory.inventory.append(leather_helmet)
        self.player_inventory.inventory.append(milk)
        leather_helmet_index = self.player_inventory.inventory.index(leather_helmet)
        self.shop.sell_item_to_shop(self.player_inventory, leather_helmet_index)
        assert self.player_inventory.inventory_gold == leather_helmet.price // 2, f'Wrong calculation. Gold should be equal {leather_helmet.price // 2},' \
                                                                                  f'not {self.player_inventory.inventory_gold}'
        assert self.player_inventory.inventory[0] == milk, f"Item wasn't sold." \
                                                           f" Got {self.player_inventory.inventory[0].name} instead of milk"

    def test_take_all_items_from_drop(self):
        for item in drop_items(2, 1):
            take_item(self.player_inventory, item)
        assert len(
            self.player_inventory.inventory) <= self.player_inventory.bag.capacity, f'You took {len(self.player_inventory.inventory)} items,' \
                                                                                    f' but inventory has only {self.player_inventory.bag.capacity} slots'

    def test_kill_enemy_and_check_dropped_gold(self):
        fight(self.player, self.rat, self.player_inventory)
        assert self.player_inventory.inventory_gold > 0, "You didn't get gold for killed enemy, but should"

    def test_equip_new_bug_and_equip_bag_with_lower_capacity(self):
        self.player_inventory.inventory.append(linen_bag)
        self.player_inventory.inventory.append(apple)
        self.player_inventory.equip_the_bag(self.player_inventory.inventory[0])
        assert self.player_inventory.inventory_size == linen_bag.capacity, f'Wrong inventory capacity after equipping a new bag.' \
                                                                           f'Should be {linen_bag.capacity}, not {self.player_inventory.inventory_size}'
        self.player_inventory.inventory.append(milk)
        started_bag_index = self.player_inventory.inventory.index(started_bag)
        self.player_inventory.equip_the_bag(self.player_inventory.inventory[started_bag_index])
        assert self.player_inventory.inventory_size == linen_bag.capacity, f"You have equipped a bag with lower capacity which is wrong"

    def test_eat_the_food_and_again_with_full_health(self):
        self.player.health = 95
        self.player_inventory.inventory.append(milk)
        self.player_inventory.eat_the_food(self.player_inventory.inventory[0], self.player)
        assert self.player.health == self.player.base_health, f"Wrong health restoration. Player should have full health = {self.player.base_health}," \
                                                              f"but current health is {self.player.health}"
        self.player_inventory.inventory.append(milk)
        self.player_inventory.eat_the_food(self.player_inventory.inventory[0], self.player)
        assert self.player.health == self.player.base_health, f"Wrong health restoration. Player should have full health = {self.player.base_health}," \
                                                              f"but current health is {self.player.health}"
        assert len(self.player_inventory.inventory) == 1, f"Food item was deleted when player tried to restore health with full health"

    def test_equip_weapon_and_check(self):
        self.player.level = 2
        self.player_inventory.inventory.append(sword)
        self.player_inventory.equip_the_weapon(sword, self.player)
        assert self.player_armor.weapon.damage == sword.damage, f"Wrong equipped weapon damage. Should be {sword.damage}," \
                                                                f"got {self.player_armor.weapon.damage} instead"

    def test_a_equip_armor_with_not_enough_level(self):
        self.player_inventory.equip_the_armor(iron_helmet, self.player)
        assert self.player_armor.calculate_total_armor() == 0, f"You equipped armor level {iron_helmet.level} with player level {self.player.level}"

    def test_equip_armor_and_equip_one_more_time(self):
        self.player.level = 7
        self.player_inventory.inventory.append(iron_helmet)
        self.player_inventory.inventory.append(leather_helmet)
        iron_helmet_index = self.player_inventory.inventory.index(iron_helmet)
        leather_helmet_index = self.player_inventory.inventory.index(leather_helmet)
        self.player_inventory.equip_the_armor(self.player_inventory.inventory[leather_helmet_index], self.player)
        assert len(self.player_inventory.inventory) == 1, f"Armor wasn't removed from inventory after equipping on empty slot!"
        assert self.player_armor.calculate_total_armor() == leather_helmet.armor, f"Wrong item was equipped." \
                                                                                  f"Should be {leather_helmet.name}, not {iron_helmet.name}"
        self.player_inventory.equip_the_armor(self.player_inventory.inventory[iron_helmet_index], self.player)
        assert self.player_inventory.inventory[0] == leather_helmet, f"{leather_helmet.name} wasn't replaced with {iron_helmet.name}."\
                                                                     f" In inventory left {self.player_inventory.inventory[0].name}"
        assert len(self.player_inventory.inventory) == 1, f"Should be only 1 armor part in inventory, not {len(self.player_inventory.inventory)}!"
        assert self.player_armor.calculate_total_armor() == iron_helmet.armor, f"Wrong item was equipped or wrong total armor calculation." \
                                                                               f"Should be {iron_helmet.armor} total armor, not {self.player_armor.calculate_total_armor()}"

    def tearDown(self):
        self.player_inventory.inventory.clear()
        self.player_warehouse.warehouse.clear()
        self.player.level = 1


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
