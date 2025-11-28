
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Bike(Vehicle):
    def ride(self):
        print("Riding a bike")

class Truck(Vehicle):
    def load(self):
        print("Loading goods in truck")

# Usage
c = Car()
c.start()   # From Vehicle
c.drive()   # From Car

b = Bike()
b.start()   # From Vehicle
b.ride()    # From Bike
