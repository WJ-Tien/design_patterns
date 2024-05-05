"""
Reduce RAM usage --> Flyweight --> separate intrinsic object and keep only one copy!
constant data: intrinsic state; otherwise (unique) extrinsic state
In this case, x, y are extr, while brand and version are intr
--> brand and version are shared among different car objects
"""


class CarType:
    # intrinsic state
    # Flyweight Class
    def __init__(self, brand: str, version: str) -> None:
        self.brand = brand
        self.version = version

    def print_car(self) -> None:
        print(f"{self.brand} + {self.version}")


class CarTypeFactory:
    # Flyweight Class's Factory
    # To build many car types

    def __init__(self) -> None:
        # key := brand + "+" + version; value = CarType(brand, version)
        self.car_types = dict()

    def get_car_type_key(self, brand: str, version: str) -> str:
        car_type_key = brand + "+" + version
        if car_type_key not in self.car_types:
            print("Does not exist, add new car_type")
            self.car_types[car_type_key] = CarType(brand, version)
        else:
            print("Exists")
        return car_type_key

    def get_car_type(self, car_type_key: str) -> str:
        return self.car_types[car_type_key]


class Car:
    # extrinsic state
    def __init__(self, x: float, y: float, car_type: CarType) -> None:
        self.x = x
        self.y = y
        self.car_type = car_type

    def print_car(self) -> None:
        self.car_type.print_car()


class CarFleet:
    def __init__(self, car_type_factory: CarTypeFactory) -> None:
        self.car_fleets = dict()
        self.car_type_factory = car_type_factory

    def add_car(self, x, y, brand, version) -> None:
        car_type_key = self.car_type_factory.get_car_type_key(brand, version)
        car_type_ins = self.car_type_factory.get_car_type(car_type_key)
        car = Car(x, y, car_type_ins)
        self.car_fleets[car] = car

    def print_car(self):
        for car in self.car_fleets:
            car.print_car()

    def print_car_fleets(self) -> None:
        print(self.car_fleets)


if __name__ == "__main__":
    ctf = CarTypeFactory()
    cf = CarFleet(ctf)
    cf.add_car(1, 1, "CarA", "v1")
    cf.add_car(1, 1, "CarB", "v1")
    cf.add_car(1, 2, "CarA", "v1")
    cf.print_car()
    cf.print_car_fleets()
