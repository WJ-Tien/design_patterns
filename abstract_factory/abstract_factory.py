"""
provide a common factory for same types but different implementation
ABC, abstractmethod are often used
"""
from abc import ABC, abstractmethod


class CarFactory(ABC):
    @abstractmethod
    def boost(self):
        

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def drift(self):
        pass


class CarA(CarFactory):
    def boost(self):
        print("CarA boosts")

    def brake(self):
        print("CarA brakes")

    def drift(self):
        print("CarA drifts")


class CarB(CarFactory):
    def boost(self):
        print("CarB boosts")

    def brake(self):
        print("CarB brakes")

    def drift(self):
        print("CarB drifts")
