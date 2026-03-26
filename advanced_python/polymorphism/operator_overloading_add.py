class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{0} + {1}i".format(self.x, self.y)

    def __add__(self, obj):
        x = self.x + obj.x
        y = self.y + obj.y
        return Complex(x, y)

c1 = Complex(5, 10)
c2 = Complex(15, 20)
print("addition of two complex numbers =", c1 + c2)
