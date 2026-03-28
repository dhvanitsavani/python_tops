class A:
    def __init__(self, a):
        self.a = a

    def printData1(self):
        print("a = ", self.a)

class B:
    def __init__(self, b):
        self.b = b

    def printData2(self):
        print("b = ", self.b)

class C(A, B):
    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c

    def printData3(self):
        print("c = ", self.c)

obj1 = C(5, 10, 20)
obj1.printData1()
obj1.printData2()
obj1.printData3()
