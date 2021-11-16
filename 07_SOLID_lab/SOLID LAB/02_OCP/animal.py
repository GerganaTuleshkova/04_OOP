from abc import ABC, abstractmethod


class Animal:
    _species = None
    _sound = None

    def __init__(self):
        self.species = self._species

    def get_species(self):
        return self.species

    def make_sound(self):
        print(self._sound)


class Cat(Animal):
    _species = "Cat"
    _sound = 'meow'


class Dog(Animal):
    _species = "Dog"
    _sound = 'woof-woof'


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()


animals = [Cat(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
