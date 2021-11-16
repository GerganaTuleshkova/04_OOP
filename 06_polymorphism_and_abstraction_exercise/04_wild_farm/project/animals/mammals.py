from project.animals.animal import Mammal


class Mouse(Mammal):
    foods = ["Vegetable", "Fruit"]
    wight_gain = 0.10

    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    foods = ["Meat"]
    wight_gain = 0.40

    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    foods = ["Meat", "Vegetable"]
    wight_gain = 0.30

    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    foods = ["Meat"]
    wight_gain = 1.00

    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
