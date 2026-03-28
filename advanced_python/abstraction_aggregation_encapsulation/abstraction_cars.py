from abc import ABC, abstractmethod

class cars(ABC):

    @abstractmethod
    def features(seats, fuel, maxSpeed):
        pass
    
class mercedes(cars):

    def display(self):
        print("we'll representing features of mercedes")

    def features(self, seats, fuel, maxSpeed):
        print("mercedes is ", seats, " seater car.")
        print("mercedes is driven on ", fuel)
        print("mercedes's max speed is ", maxSpeed)

class bmw(cars):

    def display(self):
        print("we'll representing features of bmw")

    def features(self, seats, fuel, maxSpeed):
        print("bmw is ", seats, " seater car.")
        print("bmw is driven on ", fuel)
        print("bmw's max speed is ", maxSpeed)

class toyota(cars):

    def display(self):
        print("we'll representing features of toyota")

    def features(self, seats, fuel, maxSpeed):
        print("toyota is ", seats, " seater car.")
        print("toyota is driven on ", fuel)
        print("toyota's max speed is ", maxSpeed)

class volkswagen(cars):

    def display(self):
        print("we'll representing features of volkswagen")

    def features(self, seats, fuel, maxSpeed):
        print("volkswagen is ", seats, " seater car.")
        print("volkswagen is driven on ", fuel)
        print("volkswagen's max speed is ", maxSpeed)

m1 = mercedes()
b1 = bmw()
t1 = toyota()
v1 = volkswagen()

m1.display()
m1.features(5, "petrol", 240)
print("-"*30)

b1.display()
b1.features(5, "petrol", 300)
print("-"*30)

t1.display()
t1.features(7, "diesel", 230)
print("-"*30)

v1.display()
v1.features(5, "petrol", 210)
print("-"*30)
