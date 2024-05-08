"""

Caretaker manages mementoes via originator, and use originator to control mementoes
Originator produce or use the mementoes directly

Caretaker -> originator -> memento

"""

from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters

# https://refactoring.guru/design-patterns/memento/python/example#lang-features


class Originator:
    """deal with Memento class"""

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def random_engine_generator(self) -> None:
        print("Originator: I'm starting an engine.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> "Memento":
        return ConcreteMemento(self._state)

    def restore(self, memento: "Memento") -> None:
        """
        Restores the Originator's state from a memento object.
        """

        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento(ABC):
    """
    The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it DOES NOT EXPOSE
    the Originator's state.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        The Originator uses this method when restoring its state.
        """
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker:
    """
    The main controller.
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento. It
    works with all mementos via the base Memento interface.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            print("Can't undo, please check your data.")

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    # state = "A-B-C-D-E"
    originator = Originator("A-B-C-D-E.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.random_engine_generator()

    caretaker.backup()
    originator.random_engine_generator()

    caretaker.backup()
    originator.random_engine_generator()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()
