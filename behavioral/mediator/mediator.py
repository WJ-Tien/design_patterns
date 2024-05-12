"""
All the participants share the same chatroom instance (self)
--> participant.mediator = self
By doing so, the chatroom can controll all the messages sending and receiving
Mediator acts as a controller to the components !!
Components themselves don't know each other
"""

from abc import ABC, abstractmethod
from typing import List


class Mediator(ABC):
    @abstractmethod
    def register(self, participant: "Participant") -> None:
        pass

    @abstractmethod
    def send(self, message: str, sender: "Participant") -> None:
        pass


class ChatRoom(Mediator):
    # concrete mediator
    def __init__(self) -> None:
        self.participants: List[Participant] = []

    def register(self, participant: "Participant") -> None:
        if participant not in self.participants:
            self.participants.append(participant)
            """ very critical !!! """
            participant.mediator = self

    def send(self, message: str, sender: "Participant") -> None:
        for participant in self.participants:
            if participant is not sender:  # prevent sending msgs to self
                participant.receive(message)


class Participant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.mediator: Mediator = None

    def send(self, message: str) -> None:
        print(f"{self.name} Send msgs: {message}")
        self.mediator.send(message, self)

    def receive(self, message: str) -> None:
        print(f"{self.name} Receive msgs: {message}")


if __name__ == "__main__":
    # mediator
    chat_room = ChatRoom()

    # participants
    alice = Participant("Alice")
    bob = Participant("Bob")
    charlie = Participant("Charlie")

    # register participants to the chat room
    chat_room.register(alice)
    chat_room.register(bob)
    chat_room.register(charlie)

    # send notification
    alice.send("Hello")
    bob.send("Hi Alice")
    charlie.send("Good evening everyone")
