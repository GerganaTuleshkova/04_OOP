from unittest import TestCase, main
from project.train.train import Train


class TrainTests(TestCase):
    train_name = "tu tu"
    train_capacity = 25
    TRAIN_FULL = "Train is full"
    PASSENGER_NOT_FOUND = "Passenger Not Found"

    def setUp(self) -> None:
        self.actual_train = Train(self.train_name, self.train_capacity)

    def test_init__expect_valid_instance(self):

        self.assertEqual(self.train_name, self.actual_train.name)
        self.assertEqual(self.train_capacity, self.actual_train.capacity)
        self.assertEqual([], self.actual_train.passengers)

    def test_add__with_capacity_reached__expect_value_error(self):
        self.actual_train.capacity = 0

        with self.assertRaises(ValueError) as cm:
            self.actual_train.add("Georgi")

        self.assertEqual(self.TRAIN_FULL, str(cm.exception))
        self.assertEqual(0, len(self.actual_train.passengers))

    def test_add__with_passenger_name_on_list__expect_value_error(self):
        passenger_name = "John"
        self.actual_train.add(passenger_name)

        with self.assertRaises(ValueError) as cm:
            self.actual_train.add(passenger_name)
        expected_message = f"Passenger {passenger_name} Exists"
        self.assertEqual(expected_message, str(cm.exception))
        self.assertEqual(1, len(self.actual_train.passengers))

    def test_add__with_passenger_name_not_on_list_and_free_capacity__expect_passenger_added(self):
        passenger_name = "John"
        actual_result = self.actual_train.add(passenger_name)
        expected_result = f"Added passenger {passenger_name}"

        self.assertTrue(passenger_name in self.actual_train.passengers)
        self.assertEqual(1, len(self.actual_train.passengers))
        self.assertEqual(expected_result, actual_result)

    def test_remove__with_passenger_name_not_on_list__expect_value_error(self):
        passenger_name = "John"
        existing_passenger = "Steve"
        self.actual_train.add(existing_passenger)

        with self.assertRaises(ValueError) as cm:
            self.actual_train.remove(passenger_name)

        self.assertEqual(self.PASSENGER_NOT_FOUND, str(cm.exception))
        self.assertEqual(1, len(self.actual_train.passengers))
        self.assertFalse(passenger_name in self.actual_train.passengers)

    def test_remove__with_passenger_name_on_the_list__expect_to_be_removed(self):
        passenger_name = "John"
        self.actual_train.add(passenger_name)

        actual_result = self.actual_train.remove(passenger_name)
        expected_result = f"Removed {passenger_name}"

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(0, len(self.actual_train.passengers))
        self.assertFalse(passenger_name in self.actual_train.passengers)


if __name__ == "__main__":
    main()