# Requirements
# Create an abstract class Vehicle
# abstract method: start_engine()
# Create child class Car
# implement start_engine()
# Create child class Bike
# implement start_engine()
# Create child class Bus
# implement start_engine()
# Create objects and call start_engine() method.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
     
    def brakes(self):
        print("Brakes are applied")

class Car(Vehicle):
    def start_engine(self):
        print("the car Engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("the bike Engine started")

class Bus(Vehicle):
    def start_engine(self):
        print("the bus Engine started")

c = Car()
c.start_engine()
c.brakes()




