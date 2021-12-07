from abc import ABC, abstractmethod

from project.checker import is_empty_string
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if is_empty_string(value):
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish: BaseFish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {type(fish).__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish_obj.eat() for fish_obj in self.fish]

    def __str__(self):
        return f"{self.name}:\n" \
                           f"Fish: {' '.join(f.name for f in self.fish) if self.fish else 'none'}\n" \
                           f"Decorations: {len(self.decorations)}\n" \
                           f"Comfort: {self.calculate_comfort()}"





        