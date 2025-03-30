#task

#Створити абстрактний базовий клас Vehicle з методом start_engine().
#Змінити класи Car та Motorcycle, щоб вони успадковувались від Vehicle.
#Створити абстрактний клас VehicleFactory з методами create_car() та create_motorcycle().
#Реалізувати два класи фабрики: USVehicleFactory та EUVehicleFactory. Ці фабрики повинні створювати автомобілі та мотоцикли з позначкою регіону наприклад, Ford Mustang (US Spec) відповідно для США.
#Змініть початковий код так, щоб він використовував фабрики для створення транспортних засобів.



from abc import ABC, abstractmethod
from typing import Protocol
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


def main() -> None:
    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    vehicle1: Vehicle = us_factory.create_car("Toyota", "Corolla")
    vehicle2: Vehicle = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")

    vehicle1.start_engine()
    vehicle2.start_engine()


if __name__ == "__main__":
    main()