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

class C(B):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def printData3(self):
        print("c = ", self.c)

obj1 = C(5, 15, 30)
obj1.printData1()
obj1.printData2()
obj1.printData3()
