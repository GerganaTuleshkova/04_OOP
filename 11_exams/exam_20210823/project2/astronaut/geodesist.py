from project2.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):


    def __init__(self, name):
        super().__init__(name, 50)

    def breathe(self):
        self.oxygen -= self._oxygen_needed_per_breathe