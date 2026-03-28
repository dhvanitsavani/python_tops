class A:
    def __init__(self, a):
        self.a = a
        
    def printData1(self):
        print("a = ", self.a)

class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def printData2(self):
        print("b = ", self.b)

obj1 = B(10, 20)
obj1.printData1()
obj1.printData2()
