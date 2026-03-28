class Demo:
    def __init__(self, a, b):
        print("Constructor called...")
        self.a = a
        self.b = b

    def show(self):
        print(f"a = {self.a}, b = {self.b}")

print("Not created object yet")
d1 = Demo(1, 5)
print("Created object but not called show() method yet")
d1.show()
