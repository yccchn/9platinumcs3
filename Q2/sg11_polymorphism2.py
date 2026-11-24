# 1. 
# a. Duck typing is a programming concept that focuses on what an object can do, rather than what it is. An object can be used as long as it has the needed methods and properties. Inheritance is not required because the objects only need to have the same method to work in the program.
# b.  The Car class does not need to inherit from the Animal class, it only needs to have the same method as the Dog and Cat classes so that all of them can be used in the same loop.
# 2.
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car1 = Car()
boat1 = Boat()
drone1 = Drone()

vehicles = [car1, boat1, drone1]

for vehi in vehicles:
    start_trip(vehi)