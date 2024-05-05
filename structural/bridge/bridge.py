"""
Two different classes
One act as implementation, while the other acts as abstraction
abstraction takes implementation as input, and implement methods based on impl's methods
--> abstraction calls implementation (better separation)
Prevent imple * abstract combinations of classes
Example: CarKey -> Car (car_ops)
"""

from abc import ABC, abstractmethod


class CarImplementation(ABC):
    @abstractmethod
    def open_door(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def close_door(self) -> None:
        raise NotImplementedError


class CarA(CarImplementation):
    def open_door(self) -> None:
        print("Open CarA's door")

    def close_door(self) -> None:
        print("Close CarA's door")


class CarB(CarImplementation):
    def open_door(self) -> None:
        print("Open CarB's door")

    def close_door(self) -> None:
        print("Close CarB's door")


class CarKey:
    def __init__(self, CarImpl: CarImplementation):
        self.CarImpl = CarImpl

    def open_with_key(self) -> None:
        print("Using a key to open the door")
        self.CarImpl.open_door()

    def close_with_key(self) -> None:
        print("Using a key to close the door")
        self.CarImpl.close_door()


class CarAKey(CarKey):
    def discard_key(self) -> None:
        print("Discard the key")
        self.CarImpl.close_door()


if __name__ == "__main__":
    CAR_A = CarA()
    CAR_A_KEY = CarKey(CAR_A)
    CAR_A_KEY.open_with_key()

    CAR_B = CarB()
    CAR_B_KEY = CarKey(CAR_B)
    CAR_B_KEY.open_with_key()

    CAR_A = CarA()
    CAR_A_KEY = CarAKey(CAR_A)
    CAR_A_KEY.discard_key()
