class A:
    def __init__(self,name):
        self.name=name
    def getData(self):
        self.name=input("enter the name:")
        print(self.name,"you are in A")
class B(A):
    def b1(self):
        print("your are in class B")
class C(B):
    def c1(self):
        print("you are in class C")
class D(C):
    def d1(self):
        print("you are in D")
d=D('')
d.getData()
d.b1()
d.c1()
d.d1()