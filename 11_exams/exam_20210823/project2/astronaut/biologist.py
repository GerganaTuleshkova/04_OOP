from project2.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    _oxygen_needed_per_breathe = 5

    def __init__(self, name):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= self._oxygen_needed_per_breathe