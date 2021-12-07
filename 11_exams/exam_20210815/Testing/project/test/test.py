from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTests(TestCase):
    shop_name = "Cats and Dogs"

    def setUp(self) -> None:
        self.actual_shop = PetShop(self.shop_name)

    def test_init__expect_instance(self):
        self.assertEqual(self.shop_name, self.actual_shop.name)
        self.assertEqual([], self.actual_shop.pets)
        self.assertEqual({}, self.actual_shop.food)

    def test_add_food__with_quantity_above_zero_and_food_not_in_dict__expect_food_added(self):
        food_name = "kitties"
        quantity = 25

        actual_result = self.actual_shop.add_food(food_name, quantity)
        expected_result = f"Successfully added {quantity:.2f} grams of {food_name}."
        self.assertEqual({food_name: quantity}, self.actual_shop.food)
        self.assertEqual(expected_result, actual_result)

    def test_add_food__with_quantity_above_zero_and_food_in_dict__expect_quantity_increase(self):
        food_name = "kitties"
        quantity = 25

        self.actual_shop.add_food(food_name, quantity)
        actual_result = self.actual_shop.add_food(food_name, quantity)
        expected_result = f"Successfully added {quantity:.2f} grams of {food_name}."
        self.assertEqual({food_name: quantity * 2}, self.actual_shop.food)
        self.assertEqual(expected_result, actual_result)

    def test_add_food__with_quantity_below_zero__expect_value_error(self):
        food_name = "kitties"
        quantity = -2

        with self.assertRaises(ValueError) as cp:
            self.actual_shop.add_food(food_name, quantity)

        expected_error = 'Quantity cannot be equal to or less than 0'
        self.assertEqual(expected_error, str(cp.exception))

    def test_add_food__with_quantity_zero__expect_value_error(self):
        food_name = "kitties"
        quantity = 0

        with self.assertRaises(ValueError) as cp:
            self.actual_shop.add_food(food_name, quantity)

        expected_error = 'Quantity cannot be equal to or less than 0'
        self.assertEqual(expected_error, str(cp.exception))

    def test_add_pet__with_pet_not_in_list__expect_to_be_added(self):
        pet_name = "Sharo"

        actual_result = self.actual_shop.add_pet(pet_name)
        expected_result = f"Successfully added {pet_name}."

        self.assertEqual(expected_result, actual_result)
        self.assertEqual([pet_name], self.actual_shop.pets)

    def test_add_pet__with_pet_name_in_list__expect_exception(self):
        pet_name = "Sharo"

        self.actual_shop.add_pet(pet_name)

        with self.assertRaises(Exception) as cm:
            self.actual_shop.add_pet(pet_name)

        expected_error_message = "Cannot add a pet with the same name"
        self.assertEqual(expected_error_message, str(cm.exception))

    def test_feed_pet__with_pet_name_not_in_list__expect_exception(self):
        pet_name = "Sharo"
        food_name = "kitties"

        with self.assertRaises(Exception) as cm:
            self.actual_shop.feed_pet(food_name, pet_name)

        expected_error_message = "Please insert a valid pet name"
        self.assertEqual(expected_error_message, str(cm.exception))

    def test_feed_pet_with_pet_name_in_list_and_food_name_not_in_list__expect_message(self):
        pet_name = "Sharo"
        food_name = "kitties"
        self.actual_shop.add_pet(pet_name)

        actual_result = self.actual_shop.feed_pet(food_name, pet_name)
        expected_result = f'You do not have {food_name}'

        self.assertEqual(expected_result, actual_result)

    def test_feed_pet__with_pet_name_in_list_and_food_name_in_list_and_below_hundred__expect_adding_food(self):
        pet_name = "Sharo"
        food_name = "kitties"
        food_quantity = 50
        self.actual_shop.add_pet(pet_name)
        self.actual_shop.add_food(food_name, food_quantity)

        expected_result = "Adding food..."
        actual_result = self.actual_shop.feed_pet(food_name, pet_name)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(food_quantity + 1000, self.actual_shop.food[food_name])

    def test_feed_pet__with_pet_name_in_list_and_food_name_in_list_and_above_hundred__expect_pet_feed(self):
        pet_name = "Sharo"
        food_name = "kitties"
        food_quantity = 150
        self.actual_shop.add_pet(pet_name)
        self.actual_shop.add_food(food_name, food_quantity)

        expected_result = f"{pet_name} was successfully fed"
        actual_result = self.actual_shop.feed_pet(food_name, pet_name)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(food_quantity - 100, self.actual_shop.food[food_name])

    def test_repr__expect_valid_string(self):
        pet_name_1 = "Sharo"
        self.actual_shop.add_pet(pet_name_1)

        pet_name_2 = "Puhi"
        self.actual_shop.add_pet(pet_name_2)

        expected_result = f'Shop {self.shop_name}:\n'\
                          f'Pets: {pet_name_1}, {pet_name_2}'
        actual_result = repr(self.actual_shop)

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
