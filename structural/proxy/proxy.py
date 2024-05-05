from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def operation(self) -> None:
        raise NotImplementedError


class ConcreteCar(Car):
    def operation(self) -> None:
        print("A Concrete car's operating")


class ProxyCar(Car):
    def __init__(self, concrete_car: ConcreteCar) -> None:
        self.concrete_car = concrete_car

    def operation(self) -> None:
        if self.is_valid_user():
            print("Valid user, good to go")
            self.concrete_car.operation()
        else:
            print("Invalid user")

    def is_valid_user(self) -> bool:
        return True


def client(car: Car) -> None:
    car.operation()


if __name__ == "__main__":
    concrete_car = ConcreteCar()
    client(concrete_car)

    proxy_car = ProxyCar(concrete_car)
    client(proxy_car)
