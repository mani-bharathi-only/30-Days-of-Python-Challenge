#ABSTRACT
#Abstract class act as an blueprint for the other classes."Which means like a rules for other classes"
#Without that nothing runs in other classes "which means like a rules"


from abc import ABC,abstractmethod  #importing abstract class and abstract method
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod  #decorator
    def stop(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("My Triumph Bike Started")
    def stop(self):
        print("My Bike is stopped ")

class Car(Vehicle):
    def off(self):
        print("My car is off")
    def stop(self):
        print("My Car stopped")
    def start(self):
        print("My car started")



bike=Bike()
bike.start()
bike.stop()

car=Car()
car.start()
car.off()
car.stop()