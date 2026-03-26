class A:
    def __init__(self, a, **kwargs):
        self.a = a
        super().__init__(**kwargs)

    def printData1(self):
        print("a = ", self.a)

class B(A):
    def __init__(self, b, **kwargs):
        self.b = b
        super().__init__(**kwargs)

    def printData2(self):
        print("b = ", self.b)

class C(A):
    def __init__(self, c, **kwargs):
        self.c = c
        super().__init__(**kwargs)

    def printData3(self):
        print("c = ", self.c)

class D(B, C):
    def __init__(self, a, b, c, d):
        self.d = d
        super().__init__(a=a, b=b, c=c)

    def printData4(self):
        print("d = ", self.d)

obj1 = D(a=1, b=2, c=3, d=4)
obj1.printData1()
obj1.printData2()
obj1.printData3()
obj1.printData4()
