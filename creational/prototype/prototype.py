from copy import deepcopy

class Prototype:
    def clone(self):
        return deepcopy(self)

class ConcreteProtoA(Prototype):
    def __init__(self, data):
        self.data = data

class ConcreteProtoB(Prototype):
    def __init__(self, data):
        self.data = data

class PrototypeCollections:
    def __init__(self):
        self.proto = dict() 

    def add_prototype(self, name: str, prototype: Prototype) -> None:
        self.proto[name] = prototype
    
    def get_prototype(self, name: str) -> Prototype | None:
        if name in self.proto:
            # Return deepcopy of Prototype object passed in itself !
            return self.proto[name].clone()
        else:
            return None


if __name__ == "__main__":

    protoA = ConcreteProtoA("ProtoA_Data")
    protoB = ConcreteProtoB("ProtoB_Data")

    collection = PrototypeCollections()
    collection.add_prototype("ProtoA", protoA)
    collection.add_prototype("ProtoB", protoB)

    cloned_protoA = collection.get_prototype("ProtoA")
    cloned_protoB = collection.get_prototype("ProtoB")