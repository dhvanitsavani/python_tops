from abc import ABC, abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(r):
        pass

class SBI(RBI):

    def show(self):
        print("I am SBI")

    def roi(self, r):
        print("Rate of interest given by SBI is : ", r)

class HDFC(RBI):

    def show(self):
        print("I am HDFC")

    def roi(self, r):
        print("Rate of interest given by HDFC is : ", r)

s1 = SBI()
h1 = HDFC()

s1.show()
s1.roi(2)

h1.show()
h1.roi(2.5)
