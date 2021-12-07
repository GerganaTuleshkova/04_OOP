from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    __default_increase_quantity = 2
    __default_size = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.__default_size, price)

    def eat(self):
        self.size += self.__default_increase_quantity