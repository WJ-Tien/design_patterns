"""
3rd-party lib (Adaptee) <--  Adapter ---> Default/Core code

EVehicle.special_pull_off --> error
--> need a wrapper
--> wrap special_pull_off with orginal pull_off func
--> Adaptor pattern

"""

from typing import Union


class EVehicle:
    # default EV
    def pull_off(self):
        return "EV pulled off"


class Adaptee:
    # internal combustion engine
    def special_pull_off(self):
        return "ICE pulled off SPECIAL"


class Adapter(EVehicle):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def pull_off(self) -> None:
        return f"{self.adaptee.special_pull_off()}"


def client_code(target: Union[EVehicle, Adapter]) -> None:
    return target.pull_off()


if __name__ == "__main__":
    default = EVehicle()
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(client_code(default))
    print(client_code(adapter))
