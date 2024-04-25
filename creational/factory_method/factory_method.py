"""
1. create abstract CarEngine class, with build_engine method
2. create car class, with factory_method build_car
3. create carA/carB class,modify factory_method build_car to return different return value
4. Finally it return an new object
"""

from abc import ABC, abstractmethod


class CarEngine(ABC):
    @abstractmethod
    def build_engine(self):
        raise NotImplementedError


class CarEngineA(CarEngine):
    def build_engine(self):
        return "CarEngineA"


class CarEngineB(CarEngine):
    def build_engine(self):
        return "CarEngineB"


class Car(CarEngine):
    @abstractmethod
    def build_car(self) -> CarEngine:
        pass


class CarA(Car):
    def build_car(self):
        return CarEngineA()


class CarB(Car):
    def build_car(self):
        return CarEngineB()
