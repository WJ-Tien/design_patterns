"""

Tree-like design patterns
Leaf -> Composite (Both inherit from Component class)

"""

from abc import ABC, abstractmethod
from typing import List


class CarComponent(ABC):
    def add(self) -> None:
        pass

    def remove(self) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class CarLeaf(CarComponent):
    def operation(self) -> str:
        return "CarLeaf"


class CarComposite(CarComponent):
    def __init__(self) -> None:
        self.children: List[CarComponent] = []

    def add(self, component: CarComponent) -> None:
        self.children.append(component)

    def remove(self, component: CarComponent) -> None:
        self.children.remove(component)

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results: List = []

        for child in self.children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_1(component: CarComponent) -> None:
    print(f"Result: {component.operation()}", end="")


def client_2(component1: CarComponent, component2: CarComponent) -> None:
    if component1.is_composite():
        component1.add(component2)

    print(f"Result: {component1.operation()}", end="")


if __name__ == "__main__":
    single_leaf = CarLeaf()
    tree = CarComposite()

    branch1 = CarComposite()
    branch1.add(CarLeaf())
    branch1.add(CarLeaf())

    branch2 = CarComposite()
    branch2.add(CarLeaf())
    branch2.add(CarLeaf())

    tree.add(branch1)
    tree.add(branch2)

    client_1(tree)
    print("")
    client_2(tree, single_leaf)
