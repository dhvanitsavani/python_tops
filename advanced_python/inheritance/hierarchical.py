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

class C(A):
    def __init__(self, a, c):
        super().__init__(a)
        self.c = c

    def printData2(self):
        print("c = ", self.c)

obj1 = B(5, 10)
obj2 = C(50, 100)
obj1.printData1()
obj1.printData2()
obj2.printData1()
obj2.printData2()
