from project.vehicle import Vehicle

from unittest import TestCase, main


class VehicleTests(TestCase):
    DEFAULT_FUEL_CONSUMPTION = 1.25
    fuel_consumption: float
    fuel = 50.5
    capacity: float
    horse_power = 120.5

    def setUp(self) -> None:
        self.actual_vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init__with_valid_arguments__expect_instance(self):
        self.assertEqual(self.fuel, self.actual_vehicle.fuel)
        self.assertEqual(self.horse_power, self.actual_vehicle.horse_power)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.actual_vehicle.fuel_consumption)
        self.assertEqual(self.fuel, self.actual_vehicle.capacity)

    # def test_init__with_different_default_fuel_consumption__expect_class_default(self):
    #     self.DEFAULT_FUEL_CONSUMPTION = 3
    #     self.assertEqual(1.25, self.actual_vehicle.fuel_consumption)
    #     self.DEFAULT_FUEL_CONSUMPTION = 1.25

    def test_drive__with_enough_fuel__expect_fuel_decrease(self):
        self.actual_vehicle.drive(10)
        expected_result = self.fuel - self.DEFAULT_FUEL_CONSUMPTION * 10
        self.assertEqual(expected_result, self.actual_vehicle.fuel)

    def test_drive__with_not_enough_fuel__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.actual_vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel__with_less_than_capacity_quantity__expect_fuel_increase(self):
        self.actual_vehicle.drive(30)
        self.actual_vehicle.refuel(20)
        expected_result = self.fuel - self.DEFAULT_FUEL_CONSUMPTION * 30 + 20
        self.assertEqual(expected_result, self.actual_vehicle.fuel)

    def test_refuel__with_more_than_capacity_quantity__expect_exception(self):

        with self.assertRaises(Exception) as ex:
            self.actual_vehicle.refuel(50)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str__expect_valid_string(self):
        expected_string = f"The vehicle has {self.horse_power} " \
               f"horse power with {self.fuel} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected_string, str(self.actual_vehicle))


if __name__ == "__main__":
    main()