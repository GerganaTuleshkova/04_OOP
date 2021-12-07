from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in valid_types:
            return "Invalid aquarium type."
        class_ = globals()[aquarium_type]
        aquarium_to_be_added = class_(aquarium_name)
        self.aquariums.append(aquarium_to_be_added)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        valid_types = ["Ornament", "Plant"]
        if decoration_type not in valid_types:
            return "Invalid decoration type."

        class_ = globals()[decoration_type]
        decoration_to_be_added = class_()

        self.decorations_repository.add(decoration_to_be_added)
        return f"Successfully added {decoration_type}."

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium_obj in self.aquariums:
            if aquarium_obj.name == aquarium_name:
                return aquarium_obj
        return None

    def __return_first_decoration_by_type(self, decoration_type):
        for decoration_obj in self.decorations_repository.decorations:
            if type(decoration_obj).__name__ == decoration_type:
                return decoration_obj
        return None

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration_to_add = self.__return_first_decoration_by_type(decoration_type)
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if decoration_to_add is None:
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium is None:
            return

        aquarium.add_decoration(decoration_to_add)
        self.decorations_repository.remove(decoration_to_add)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type not in valid_fish_types:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return

        if not type(aquarium).__name__[:4] == fish_type[:4]:
            return "Water not suitable."

        class_ = globals()[fish_type]
        fish_to_be_added = class_(fish_name, fish_species, price)
        result = aquarium.add_fish(fish_to_be_added)
        return result

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if aquarium is None:
            return

        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if aquarium is None:
            return

        value = 0
        value += sum([f.price for f in aquarium.fish])
        value += sum([d.price for d in aquarium.decorations])

        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        # new_line = '\n'
        # return f"{new_line.join([str(a) for a in self.aquariums])}"

        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"
        return result.strip()


