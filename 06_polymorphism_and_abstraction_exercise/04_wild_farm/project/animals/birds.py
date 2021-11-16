from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    foods = ["Meat"]
    wight_gain = 0.25

    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    foods = ["Meat", "Vegetable", "Fruit", "Seed"]
    wight_gain = 0.35

    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"
