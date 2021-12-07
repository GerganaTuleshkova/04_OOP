from project2.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    _oxygen_needed_per_breathe = 15

    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= self._oxygen_needed_per_breathe
