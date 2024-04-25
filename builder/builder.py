"""
Car -> store the esstential elements of a car
CarBuilder -> builder w/ different functions
Director -> To assign builder to build Car

Focusing on a set of construction functions
Return self (chaining) is critical !

"""


class Car:
    def __init__(self, builder: "CarBuilder"):
        self.door_counts = builder.door_counts
        self.tire_counts = builder.tire_counts


class CarBuilder:
    def __init__(self):
        self.door_counts = None
        self.tire_counts = None

    def set_door_counts(self, door_counts: int) -> "CarBuilder":
        self.door_counts = door_counts
        return self

    def set_tire_counts(self, tire_counts: int) -> "CarBuilder":
        self.tire_counts = tire_counts
        return self

    def build(self):
        return Car(self)


class Director:
    def __init__(self, builder: "CarBuilder"):
        self.builder = builder

    def build_a_car(self) -> "CarBuilder":
        return self.builder.set_door_counts(4).set_tire_counts(4).build()


if __name__ == "__main__":
    director = Director(CarBuilder())
    new_car = director.build_a_car()
    print(new_car.door_counts)
    print(new_car.tire_counts)
