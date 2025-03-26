#task

#Створити абстрактний базовий клас Vehicle з методом start_engine().
#Змінити класи Car та Motorcycle, щоб вони успадковувались від Vehicle.
#Створити абстрактний клас VehicleFactory з методами create_car() та create_motorcycle().
#Реалізувати два класи фабрики: USVehicleFactory та EUVehicleFactory. Ці фабрики повинні створювати автомобілі та мотоцикли з позначкою регіону наприклад, Ford Mustang (US Spec) відповідно для США.
#Змініть початковий код так, щоб він використовував фабрики для створення транспортних засобів.



from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Мотор заведено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Toyota", "Corolla")
vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")

vehicle1.start_engine()
vehicle2.start_engine()