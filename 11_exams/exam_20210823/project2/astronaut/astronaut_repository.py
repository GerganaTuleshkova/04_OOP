#from astronaut.astronaut import Astronaut
from project2.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            return
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut not in self.astronauts:
            return
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut_obj in self.astronauts:
            if astronaut_obj.name == name:
                return astronaut_obj
        return None


