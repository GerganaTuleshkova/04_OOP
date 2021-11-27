from extended_list import IntegerList

from unittest import TestCase, main


class IntegersListTest(TestCase):
    def setUp(self) -> None:
        self.actual_list = IntegerList(1, 2, 3)

    def test_init__with_agrs_integers__expect_valid_instance(self):
        self.assertEqual([1, 2, 3], self.actual_list._IntegerList__data)

    def test_init__with_agrs_not_integers__expect_valid_instance(self):
        actual_list = IntegerList("1", 2, 3)
        self.assertEqual([2, 3], actual_list._IntegerList__data)

    def test_add__with_valid_integer__expect_element_added(self):
        self.actual_list.add(4)
        self.assertEqual([1, 2, 3, 4], self.actual_list._IntegerList__data)

    def test_add__with_string__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.actual_list.add("0")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add__with_float__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.actual_list.add(5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add__with_bool__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.actual_list.add(False)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add__with_none__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.actual_list.add(None)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index__with_valid_index__expect_element_at_index_removed(self):
        self.actual_list.remove_index(0)
        self.assertEqual([2, 3], self.actual_list._IntegerList__data)

    def test_remove_index__with_index_higher_than_len__expect_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.actual_list.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get__with_valid_index__expect_element_returned(self):
        expected_element = self.actual_list.get(0)
        self.assertEqual(1, expected_element)

    def test_get__with_index_higher_than_len__expect_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.actual_list.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert__with_valid_index_and_integer__expect_element_added(self):
        self.actual_list.insert(0, 5)
        self.assertEqual([5, 1, 2, 3], self.actual_list._IntegerList__data)

    def test_insert__with_index_higher_than_len__expect_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.actual_list.insert(3, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert__with_valid_index_and_not_integer__expect_index_error(self):
        with self.assertRaises(ValueError) as ex:
            self.actual_list.insert(0, "5")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest__expect_biggest_element_returned(self):
        actual_biggest = self.actual_list.get_biggest()
        self.assertEqual(3, actual_biggest)

    def test_get_index__expect_valid_index_returned(self):
        actual_index = self.actual_list.get_index(3)
        self.assertEqual(2, actual_index)


if __name__ == "__main__":
    main()