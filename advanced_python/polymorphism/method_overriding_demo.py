# Defination of method overriding :-
''' When there is a same method prototype in your both baseclass and derived class and
    if you call that method using the object of derived class, then only derived class
    method will be called. So you can say that method of derived class overrides the
    method of base class. '''
class A:
    def show(self):
        print("showed from class A")

class B(A):
    def show(self):
        print("showed from class B")

class C(B):
    def show(self):
        print("showed from class C")

c1 = C()
c1.show()
