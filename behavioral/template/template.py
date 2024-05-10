from abc import ABC, abstractmethod


class CarTemplate(ABC):
    @abstractmethod
    def Boost(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def Stop(self) -> None:
        raise NotImplementedError

    def check(self) -> None:
        print("Check in")


class CarA:
    def Boost(self) -> None:
        print("CarA boosts")

    def Stop(self) -> None:
        print("CarA Stops")


class CarB:
    def Boost(self) -> None:
        print("CarB boosts")

    def Stop(self) -> None:
        print("CarB Stops")
