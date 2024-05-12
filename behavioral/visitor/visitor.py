"""A visitor visits elements (accept)
An element accepts a visitor (to let it visit itself)
"""

from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def operation_a(self):
        return "ConcreteElementA"


class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def operation_b(self):
        return "ConcreteElementB"


class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass


class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"ConcreteVisitor1: {element.operation_a()}")

    def visit_concrete_element_b(self, element):
        print(f"ConcreteVisitor1: {element.operation_b()}")


class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"ConcreteVisitor2: {element.operation_a()}")

    def visit_concrete_element_b(self, element):
        print(f"ConcreteVisitor2: {element.operation_b()}")


def client_code(elements, visitor):
    for element in elements:
        element.accept(visitor)


if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]

    print("ConcreteVisitor1:")
    visitor1 = ConcreteVisitor1()
    client_code(elements, visitor1)

    print("ConcreteVisitor2:")
    visitor2 = ConcreteVisitor2()
    client_code(elements, visitor2)
