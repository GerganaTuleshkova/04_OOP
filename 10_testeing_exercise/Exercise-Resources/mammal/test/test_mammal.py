from project.mammal import Mammal

from unittest import TestCase, main


class MammalTests(TestCase):
    name = "Bunny"
    mammal_type = "mammal"
    sound = "cvi cvi"

    def setUp(self) -> None:
        self.actual_mammal = Mammal(self.name, self.mammal_type, self.sound)

    def test_init_with_valid_input__expect_instance(self):
        self.assertEqual(self.name, self.actual_mammal.name)
        self.assertEqual(self.mammal_type, self.actual_mammal.type)
        self.assertEqual(self.sound, self.actual_mammal.sound)
        self.assertEqual("animals", self.actual_mammal._Mammal__kingdom)

    def test_make_sound__expect_valid_string(self):
        actual_result = self.actual_mammal.make_sound()
        expected_result = f"{self.name} makes {self.sound}"
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom__expect_valid_string(self):
        self.assertEqual("animals", self.actual_mammal.get_kingdom())

    def test_info__expect_valid_string(self):
        expected_result = f"{self.name} is of type {self.mammal_type}"
        actual_result = self.actual_mammal.info()
        self.assertEqual(expected_result, actual_result)
