"""
user --> Facade --> complex or 3rd party modules
"""

from typing import List


class Facade:
    def __init__(self, car_A, car_B) -> None:
        self.car_A = car_A
        self.car_B = car_B

    def operation(self) -> str:
        results: List = []
        results.append(self.car_A.operation())
        results.append(self.car_B.operation())
        return "+".join(results)


class CarA:
    def operation(self) -> str:
        return "CarAStart"


class CarB:
    def operation(self) -> str:
        return "CarBStart"


def client(facade: Facade) -> None:
    print(facade.operation(), end="")


if __name__ == "__main__":
    car_A = CarA()
    car_B = CarB()
    facade = Facade(car_A, car_B)
    client(facade)
