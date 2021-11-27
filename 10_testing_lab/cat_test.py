from cat import Cat

from unittest import TestCase, main


class CatTests(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Puhi")

    def test_init_expect_valid_attributes(self):
        self.assertEqual("Puhi", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat__when_fed_is_false__expect_size_increase(self):
        #self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__when_fed_is_true__expect_raises_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat__when_fed_is_false__expect_fed_true(self):
        #self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat__when_fed_is_false__expect_sleepy_true(self):
        #self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_sleep__when_fed_false__expect_raises_exception(self):
        #self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_sleep__when_fed_true__expect_sleepy_false(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()