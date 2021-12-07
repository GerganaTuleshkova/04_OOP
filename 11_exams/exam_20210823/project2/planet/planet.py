
class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    def __str__(self):
        return f"Planet {self.name} with items: {', '.join(self.items)}"
