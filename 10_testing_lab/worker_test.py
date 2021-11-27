from worker import Worker

from unittest import TestCase, main


class WorkerTests(TestCase):
    name = "Brat Pitt"
    salary = 25000
    energy = 10

    def setUp(self) -> None:
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_init_with_valid_name_salary_energy_expect_valid_attributes(self):
        # Arrange is done with setUp
        # Act is done with setUp
        # Assert
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_rest_expect_increased_energy(self):
        # Arrange is done with setUp
        # Act
        self.worker.rest()
        # Assert
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_work_with_negative_energy_expect_error(self):
        # Arrange
        worker = Worker(self.name, self.salary, -1)
        # Act & Asert
        with self.assertRaises(Exception) as ex:
            worker.work()
        # Assert
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_with_0_energy_expect_error(self):
        # Arrange
        worker = Worker(self.name, self.salary, 0)
        # Act & Asert
        with self.assertRaises(Exception) as ex:
            worker.work()
        # Assert
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_with_positive_energy_expect_energy_decrease(self):
        # Arrange is done with setUp
        # Act
        self.worker.work()
        # Assert
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_work_with_positive_energy_expect_money_increase(self):
        # Arrange is done with setUp
        # Act - 2 times in order to check that money is not set to salary but increased with salary
        self.worker.work()
        self.worker.work()
        # Assert
        self.assertEqual(self.salary*2, self.worker.money)

    def test_get_info_expect_valid_string(self):
        # Arrange is done with setUp
        # Act
        actual_result = self.worker.get_info()
        # Assert
        expected_result = f"{self.name} has saved {0} money."
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
