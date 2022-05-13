class A:
    def __init__(self):
        print("init in A")
    def display1(self):
        print("parent class method")
class B(A):
    def __init__(self):
        super().__init__()
        print("init in B")
    def display2(self):
        print("child class method")
obj=B()
obj.display1()
obj.display2()
'''class B inherit class A.If we create two class with class A contain init function
 it execute class A init.if we add both  class init function only subclass execute its init function.
 to inherite all method in super class we use keyword super().__init__() .it print both init methods
'''