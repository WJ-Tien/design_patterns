"""Context (selected strategy)
-> call context's common method
-> call strategy's common util
-> execute selected strategy"""

from abc import ABC, abstractmethod
from typing import Any


class Context:
    """interface clients"""

    def __init__(self, strategy: "Strategy") -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> "Strategy":
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: "Strategy") -> None:
        self._strategy = strategy

    def execute_selected_strategy(self):
        self._strategy.execute_strategy()


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def execute_strategy(self) -> Any:
        pass


class AddStrategy(Strategy):
    def execute_strategy(self) -> None:
        print("I am adding")


class SubStrategy(Strategy):
    def execute_strategy(self) -> None:
        print("I am substracting")


if __name__ == "__main__":
    context = Context(AddStrategy())
    context.execute_selected_strategy()
    context.strategy = SubStrategy()
    context.execute_selected_strategy()
