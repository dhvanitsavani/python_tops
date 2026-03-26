class rectangle:
    def __init__(self, *args):
        if len(args) == 0:
            self.height = 1
            self.width = 1
        elif len(args) == 1:
            self.height = args[0]
            self.width = args[0]
        else:
            self.height = args[0]
            self.width = args[1]

    def area(self):
        self.area = self.height * self.width

        print("area of rectangle = ", self.area)

r1 = rectangle()
r2 = rectangle(4)
r3 = rectangle(2, 4)

r1.area()
r2.area()
r3.area()
