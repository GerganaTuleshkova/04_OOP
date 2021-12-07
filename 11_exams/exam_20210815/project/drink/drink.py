from abc import ABC, abstractmethod

from project.checker import Checker


class Drink(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: int, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = Checker.check_string(value)

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        self.__portion = Checker.check_number(value, "Portion cannot be less than or equal to zero!")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = Checker.check_string(value, "Brand cannot be empty string or white space!")

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"


