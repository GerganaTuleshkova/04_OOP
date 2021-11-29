from project.hero import Hero

from unittest import TestCase, main


class HeroTests(TestCase):
    username = "King"
    health = 100
    damage = 50
    level = 3

    enemy_username = "Mark"
    enemy_health = 50
    enemy_damage = 50
    enemy_level = 3

    def setUp(self) -> None:
        self.actual_hero = Hero(self.username, self.level, self.health, self.damage)
        self.enemy_hero = Hero(self.enemy_username, self.enemy_level, self.enemy_health, self.enemy_damage)

    def test__init__with_valid_input__expect_instance(self):
        self.assertEqual(self.username, self.actual_hero.username)
        self.assertEqual(self.health, self.actual_hero.health)
        self.assertEqual(self.damage, self.actual_hero.damage)
        self.assertEqual(self.level, self.actual_hero.level)

    def test_battle__with_same_hero__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.actual_hero.battle(self.actual_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle__with_zero_health__expect_exception(self):
        health = 0
        actual_hero = Hero(self.username, self.level, health, self.damage)
        with self.assertRaises(ValueError) as ex:
            actual_hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle__with_negative_health__expect_exception(self):
        health = -2
        actual_hero = Hero(self.username, self.level, health, self.damage)
        with self.assertRaises(ValueError) as ex:
            actual_hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle__with_negative_enemy_health__expect_exception(self):
        health = -2
        enemy_hero = Hero(self.enemy_username, self.enemy_level, health, self.enemy_damage)
        with self.assertRaises(ValueError) as ex:
            self.actual_hero.battle(enemy_hero)
        expected_error_message = f"You cannot fight {self.enemy_username}. He needs to rest"
        self.assertEqual(expected_error_message, str(ex.exception))

    def test_battle__with_zero_enemy_health__expect_exception(self):
        health = 0
        enemy_hero = Hero(self.enemy_username, self.enemy_level, health, self.enemy_damage)
        with self.assertRaises(ValueError) as ex:
            self.actual_hero.battle(enemy_hero)
        expected_error_message = f"You cannot fight {self.enemy_username}. He needs to rest"
        self.assertEqual(expected_error_message, str(ex.exception))

    def test_battle__with_both_losing__expect_draw(self):
        expected_result = "Draw"
        actual_result = self.actual_hero.battle(self.enemy_hero)
        self.assertEqual(expected_result, actual_result)

    def test_battle__with_hero_winning__expect_winning(self):
        # Arrange
        actual_hero = Hero(self.username, self.level, self.health, 5)
        enemy_hero = Hero(self.enemy_username, self.enemy_level, self.enemy_health, self.enemy_damage)

        expected_result = "You lose"
        actual_result = actual_hero.battle(enemy_hero)
        self.assertEqual(expected_result, actual_result)

        expected_enemy_health = self.enemy_health - (actual_hero.level * actual_hero.damage) + 5
        self.assertEqual(expected_enemy_health, enemy_hero.health)

        self.assertEqual(self.enemy_level + 1, enemy_hero.level)
        self.assertEqual(self.enemy_damage + 5, enemy_hero.damage)

    def test_battle__with_hero_losing__expect_losing(self):
        # Arrange
        actual_hero = Hero(self.username, self.level, self.health, self.damage)
        enemy_hero = Hero(self.enemy_username, self.enemy_level, self.enemy_health, 5)

        expected_result = "You win"
        actual_result = actual_hero.battle(enemy_hero)
        self.assertEqual(expected_result, actual_result)

        expected_health = self.health - (enemy_hero.level * enemy_hero.damage) + 5
        self.assertEqual(expected_health, actual_hero.health)

        self.assertEqual(self.level + 1, actual_hero.level)
        self.assertEqual(self.damage + 5, actual_hero.damage)

    def test_str__expect_valid_string(self):
        expected_string = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(expected_string, self.actual_hero.__str__())


if __name__ == "__main__":
    main()