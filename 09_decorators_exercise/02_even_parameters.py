from functools import wraps


def is_number(arg):
    return isinstance(arg, int)


def is_even(n):
    return n % 2 == 0


def even_parameters(func):
    @wraps(func)
    def wrapper(*args):

        for arg in args:
            if not (is_number(arg) and is_even(arg)):
                return "Please use only even numbers!"
        return func(*args)
    return wrapper


import unittest


class EvenParametersTests(unittest.TestCase):
    def test_even(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, 4, 4)
        self.assertEqual(result, 12)

    def test_odd(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, 5, 4)
        self.assertEqual(result, "Please use only even numbers!")

    def test_with_non_integer_params(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, "4", 4)
        self.assertEqual(result, "Please use only even numbers!")

    def test_with_no_params(self):
        @even_parameters
        def func():
            return "hi"

        result = func()
        self.assertEqual(result, "hi")


if __name__ == '__main__':
    unittest.main()
