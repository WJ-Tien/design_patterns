"""
command -> command interface (has certain common funcs e.g. execute)
-> execute send request to execute funcs in the receiver
Invoker -> set command
receiver -> actual executor; real business logic

client -> invoker -> send/set command -> (receiver)

"""

from abc import ABC, abstractmethod

# https://refactoring.guru/design-patterns/command/python/example#lang-features


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class CarSimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"CarSimpleCommand: {self._payload}")


class CarComplexCommand(Command):
    def __init__(self, receiver: "Receiver", left_rm: str, right_rm: str) -> None:
        self._receiver = receiver
        self._left_rm = left_rm
        self._right_rm = right_rm

    def execute(self) -> None:
        """can delegate methods to receiver"""
        print("CarComplexCommand doing sth")
        self._receiver.do_something(self._left_rm)
        self._receiver.do_something_else(self._right_rm)


class Receiver:
    """
    Actual business logic
    """

    def do_something(self, left_rm: str) -> None:
        print(f"\nReceiver: Working on ({left_rm}.)")

    def do_something_else(self, right_rm: str) -> None:
        print(f"\nReceiver: Also working on ({right_rm}.)")


class Invoker:
    """Sender"""

    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    receiver = Receiver()
    invoker.set_on_start(CarSimpleCommand("Engine Starts"))
    invoker.set_on_finish(CarComplexCommand(receiver, "Send notification", "Save it"))

    invoker.do_something_important()
