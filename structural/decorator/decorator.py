"""
Both ConcreteComponent and Decorator inherit from CarComponent

Call ConcreteB operation  --> Call A operation --> Call basic operation
--> CDecB(CDecA(c1)); CDecA(c1) --> call c1 operation

"""


class CarComponent:
    def operation(self) -> str:
        pass


class ConcreteCarComponent(CarComponent):
    def operation(self) -> str:
        return "ConcreteCar"


class CarDecorator(CarComponent):
    def __init__(self, component: CarComponent) -> None:
        self._component = component

    @property
    def component(self) -> CarComponent:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteCarADecorator(CarDecorator):
    def operation(self) -> str:
        return f"ConcreteCarADecorator({self.component.operation()})"


class ConcreteCarBDecorator(CarDecorator):
    def operation(self) -> str:
        return f"ConcreteCarBDecorator({self.component.operation()})"


def client(component: CarComponent) -> None:
    print(f"RESULT: {component.operation()}")


if __name__ == "__main__":
    c1 = ConcreteCarComponent()
    # client(c1)
    d1 = ConcreteCarADecorator(c1)
    client(d1)
    d2 = ConcreteCarBDecorator(d1)
    client(d2)
