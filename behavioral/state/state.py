"""
State design pattern is to trace state changes
Context: control the flow of state changes (methods included)
State: control state
In this case: Context(new) -> transition to A -> transiton to B

"""

from abc import ABC, abstractmethod

# https://refactoring.guru/design-patterns/state/python/example#lang-features


class Context:
    _state = None

    def __init__(self, state: "State") -> None:
        self.transition_to(state)

    def transition_to(self, state: "State") -> None:
        self._state = state
        self._state.context = self

    def request1(self) -> None:
        self._state.handle1()

    def request2(self) -> None:
        self._state.handle2()


class State(ABC):
    _context = None

    @property
    def context(self) -> Context:
        return self._context

    # history
    # transition to another state
    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
