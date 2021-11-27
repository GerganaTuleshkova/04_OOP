from car_manager import Car

from unittest import TestCase, main


class CarTests(TestCase):
    make = "Honda"
    model = "Accord"
    fuel_consumption = 5
    fuel_capacity = 60

    def setUp(self) -> None:
        self.actual_car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        print(self.actual_car)

    def test_init__with_valid_arguments__expect_instance(self):
        self.assertEqual(self.make, self.actual_car.make)
        self.assertEqual(self.model, self.actual_car.model)
        self.assertEqual(self.fuel_consumption, self.actual_car.fuel_consumption)
        self.assertEqual(self.fuel_capacity, self.actual_car.fuel_capacity)
        self.assertEqual(0, self.actual_car.fuel_amount)

    def test_init__with_empty_string_for_make__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            Car("", self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_init__with_none_for_make__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            Car(None, self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_init__with_empty_string_for_model__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            Car(self.make, "", self.fuel_consumption, self.fuel_capacity)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_init__with_none_for_model__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            Car(self.make, None, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_init__with_zero_fuel_capacity__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            Car(self.make, self.model, self.fuel_consumption, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_init__with_negative_fuel_capacity__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            Car(self.make, self.model, self.fuel_consumption, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_init__with_zero_fuel_consumption__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            Car(self.make, self.model, 0, self.fuel_capacity)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_init__with_negative_fuel_consumption__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            Car(self.make, self.model, -1, self.fuel_capacity)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_refuel__with_positive_fuel_expect_amount_increased(self):
        self.actual_car.refuel(10)
        self.actual_car.refuel(10)
        self.assertEqual(20, self.actual_car.fuel_amount)

    def test_refuel__with_negative_fuel_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.actual_car.refuel(-3)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel__with_zero_fuel_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.actual_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel__with_positive_fuel_higher_than_capacity_expect_amount_increased_to_capacity(self):
        self.actual_car.refuel(80)
        self.assertEqual(self.fuel_capacity, self.actual_car.fuel_amount)

    def test_drive__with_enough_fuel__expect_fuel_decrease(self):
        self.actual_car.refuel(50)
        self.actual_car.drive(100)
        self.assertEqual(50 - 100 * self.fuel_consumption / 100, self.actual_car.fuel_amount)

    def test_drive__with_not_enough_fuel__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.actual_car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()