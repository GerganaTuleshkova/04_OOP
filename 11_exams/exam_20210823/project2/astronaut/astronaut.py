from abc import ABC, abstractmethod


class Astronaut(ABC):
    _oxygen_needed_per_breathe = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, oxygen: int):
        self.oxygen += oxygen

    def __str__(self):
        return f"Astronaut of type {self.__class__.__name__} with name {self.name} and with {self.oxygen}"


