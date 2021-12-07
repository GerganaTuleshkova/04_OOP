from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    __default_price = 5
    __default_comfort = 1

    def __init__(self):
        super().__init__(self.__default_comfort, self.__default_price)
