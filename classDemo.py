class A:
    def getData(self, data):
        self.data = data
    
    def printData(self):
        print(self.data)

object_1 = A()
object_1.getData("Hello I am Object")
object_1.printData()

class B:
    def __init__(self, data):
        self.data = data
        print("constructor(magic function) called")

    def printData(self):
        print(self.data)

object_2 = B("Helo I am object")
object_2.printData()
    
