from abc import ABC, abstractmethod

from project.checker import is_empty_string, is_not_positive


class BaseFish(ABC):
    __default_increase_quantity = 5

    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if is_empty_string(value):
            raise ValueError("Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        if is_empty_string(value):
            raise ValueError("Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if is_not_positive(value):
            raise ValueError("Price cannot be equal to or below zero.")
        self.__price = value

    def eat(self):
        self.size += self.__default_increase_quantity

    def __repr__(self):
        return f"Fish of type {self.__class__.__name__}" \
               f", a specie {self.species}, has size {self.size} and price {self.price}"
