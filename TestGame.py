import unittest
from classes import *
from functions import *


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player = Player("Dmitry", 1, 100, 100, 10)
        self.player_inventory = Player.Inventory(2, started_bag)
        self.player_warehouse = Player.Warehouse(5)
        self.shop = Shop()
        self.rat = Unit("Rat", 1, 50, 50, 5)

    def test_restore_health(self):
        self.player.health = 80
        self.player.restore_health(11)
        assert self.player.health == 91, f'wrong amount health was restored. Should be 91, not {self.player.health}'
        self.player.restore_health(10)
        assert self.player.health == 100, f'wrong amount health was restored. Should be 100, not {self.player.health}'

    def test_buy_item_from_shop(self):
        Player.Inventory.inventory_gold = 5
        bread_index = self.shop.goods.index(bread)
        self.shop.buy_item_from_shop(bread_index + 1)
        assert Player.Inventory.inventory_gold == 5 - bread.price, f'Wrong calculation. Gold left should be equal {5 - bread.price},' \
                                                                   f' not {Player.Inventory.inventory_gold}'
        assert self.player_inventory.inventory[0] == bread, f'Wrong bought item. Should be bread,' \
                                                            f'got {self.player_inventory.inventory[0].name} instead'

    def test_sell_item_to_shop(self):
        Player.Inventory.inventory_gold = 0
        self.player_inventory.inventory.append(leather_helmet)
        self.player_inventory.inventory.append(milk)
        self.shop.sell_item_to_shop(leather_helmet)
        assert Player.Inventory.inventory_gold == leather_helmet.price // 2, f'Wrong calculation. Gold should be equal {leather_helmet.price // 2},' \
                                                                             f'not {Player.Inventory.inventory_gold}'
        assert self.player_inventory.inventory[0] == milk, f"Item wasn't sold." \
                                                           f" Got {self.player_inventory.inventory[0].name} instead of milk"

    def test_take_all_items_from_drop(self):
        for item in drop_items(4):
            take_item(self.player_inventory, item)
        assert len(
            self.player_inventory.inventory) == self.player_inventory.bag.capacity, f'You took {len(self.player_inventory.inventory)} items,' \
                                                                                    f' but inventory has only {self.player_inventory.bag.capacity} slots'

    def test_kill_enemy_and_check_dropped_gold(self):
        fight(self.player, self.rat)
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
        self.player_inventory.inventory[0].eat_the_food(self.player)
        assert self.player.health == self.player.base_health, f"Wrong health restoration. Player should have full health = {self.player.base_health}," \
                                                              f"but current health is {self.player.health}"
        print("current health is {self.player.health} = ", self.player.health)
        self.player_inventory.inventory[0].eat_the_food(self.player)
        assert self.player.health == self.player.base_health, f"Wrong health restoration. Player should have full health = {self.player.base_health}," \
                                                              f"but current health is {self.player.health}"

    def tearDown(self):
        self.player_inventory.inventory.clear()
        self.player_warehouse.warehouse.clear()


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()