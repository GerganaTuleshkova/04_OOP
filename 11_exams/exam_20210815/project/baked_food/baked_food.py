from abc import ABC, abstractmethod

from project.checker import Checker


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = Checker.check_string(value)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):

        self.__price = Checker.check_number(value, "Price cannot be less than or equal to zero!" )

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
