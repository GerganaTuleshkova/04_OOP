from project2.astronaut.astronaut import Astronaut
from project2.astronaut.astronaut_repository import AstronautRepository
from project2.astronaut.biologist import Biologist
from project2.astronaut.geodesist import Geodesist
from project2.astronaut.meteorologist import Meteorologist
from project2.planet.planet import Planet
from project2.planet.planet_repository import PlanetRepository


class SpaceStation:
    _valid_type_names = [
        "Biologist",
        "Geodesist",
        "Meteorologist"
    ]
    _successful_missions_count = 0
    _not_successful_missions_count = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self._valid_type_names:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        class_ = globals()[astronaut_type]
        astronaut_to_be_added = class_(name)
        self.astronaut_repository.add(astronaut_to_be_added)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet_to_be_added = Planet(name)
        planet_to_be_added.items = items.split(", ")
        self.planet_repository.add(planet_to_be_added)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        if self.astronaut_repository.find_by_name(name) is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        astronaut_to_remove = self.astronaut_repository.find_by_name(name)
        self.astronaut_repository.remove(astronaut_to_remove)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        increase_volume = 10
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(increase_volume)

    def choose_astronauts_for_mission(self):
        suitable_astronauts = {}
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen <= 30:
                continue
            suitable_astronauts[astronaut] = astronaut.oxygen
        suitable_astronauts = sorted(suitable_astronauts.items(), key=lambda x: -x[1])
        if len(suitable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        if len(suitable_astronauts) > 5:
            return [x[0] for x in suitable_astronauts[:5]]
        if len(suitable_astronauts) <= 5:
            return [x[0] for x in suitable_astronauts]

    def go_to_planet(self, astronaut: Astronaut, planet: Planet):
        while planet.items:
            astronaut.backpack.append(planet.items.pop())
            astronaut.breathe()
            if astronaut.oxygen <= 0:
                return
        return

    def send_on_mission(self, planet_name: str):
        if self.planet_repository.find_by_name(planet_name) is None:
            raise Exception("Invalid planet name!")

        astronauts_on_mission = self.choose_astronauts_for_mission()

        planet_to_explore = self.planet_repository.find_by_name(planet_name)
        number_of_astronauts_gone_in_space = 0

        for astronaut in astronauts_on_mission:
            number_of_astronauts_gone_in_space += 1
            self.go_to_planet(astronaut, planet_to_explore)
            if not planet_to_explore.items:
                self._successful_missions_count += 1
                return f"Planet: {planet_name} was explored. " \
                       f"{number_of_astronauts_gone_in_space} astronauts participated in collecting items."

        if planet_to_explore.items:
            self._not_successful_missions_count += 1
            return "Mission is not completed."

    def report(self):
        resulting_string = f"{self._successful_missions_count} successful missions!\n" \
                           f"{self._not_successful_missions_count} missions were not completed!\n" \
                           f"Astronauts' info:\n"
        for astronaut_obj in self.astronaut_repository.astronauts:
            astronaut_string = f"Name: {astronaut_obj.name}\n" \
                               f"Oxygen: {astronaut_obj.oxygen}\n" \
                               f"Backpack items: "
            items_collected = ""
            if not astronaut_obj.backpack:
                items_collected = "none"
            else:
                items_collected = ", ".join(astronaut_obj.backpack)

            astronaut_string += items_collected + "\n"
            resulting_string += astronaut_string
        return resulting_string.strip()







