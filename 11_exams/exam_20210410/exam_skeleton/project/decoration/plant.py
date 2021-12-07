from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    __default_price = 10
    __default_comfort = 5

    def __init__(self):
        super().__init__(self.__default_comfort, self.__default_price)
