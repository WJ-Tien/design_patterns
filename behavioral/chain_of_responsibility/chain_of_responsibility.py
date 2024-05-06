"""
CoR: call handler (next_handler) over and over again
next_handler here stores "next handler"
with next_handler is not None, we can call next_handler's handle method

"""

from abc import ABC, abstractmethod
from typing import Optional, Union


class CarHandler(ABC):
    @abstractmethod
    def set_next(self, handler: "CarHandler") -> "CarHandler":
        pass

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        pass


class AbstractCarHandler(CarHandler):
    _next_handler: CarHandler = None

    def set_next(self, handler: CarHandler) -> CarHandler:
        self._next_handler = handler
        return self._next_handler

    @abstractmethod
    def handle(self, request: str) -> Union[str, None]:
        if self._next_handler:
            return self._next_handler.handle(request)


class CarAHandler(AbstractCarHandler):
    def handle(self, request: str) -> Union[str, CarHandler]:
        if request == "CarA":
            return f"{request} handling"
        return super().handle(request)


class CarBHandler(AbstractCarHandler):
    def handle(self, request: str) -> Union[str, CarHandler]:
        if request == "CarB":
            return f"{request} handling"
        return super().handle(request)


class CarCHandler(AbstractCarHandler):
    def handle(self, request: str) -> Union[str, CarHandler]:
        if request == "CarC":
            return f"{request} handling"
        return super().handle(request)


def client(handler: CarHandler) -> None:
    cars = ["CarA", "CarB", "CarC"]
    for car in cars:
        result = handler.handle(car)
        if result:
            print(f"{result}", end="+")
        else:
            print("Nothing happened", end="+")
    print("")


if __name__ == "__main__":
    carA = CarAHandler()
    carB = CarBHandler()
    carC = CarCHandler()

    carA.set_next(carB).set_next(carC)
    # A -> B -> C -> None
    client(carA)
    client(carB)
