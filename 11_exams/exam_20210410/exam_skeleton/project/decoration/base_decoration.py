from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    @abstractmethod
    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price

    def __repr__(self):
        return f"Decoration of type {self.__class__.__name__} with price {self.price} and comfort {self.comfort}."
