from abc import abstractmethod, ABC
from project.food import Food


class Animal(ABC):
    foods = []
    wight_gain = 0.0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.foods:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.wight_gain * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


