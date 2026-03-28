class Demo:
    def add(self, a, b):
        self.a = a
        self.b = b
        self.ans = self.a + self.b

        print("Addition : ", self.a + self.b)

d1 = Demo()
d1.add(2, 3)
print("Addition : ", d1.ans)
