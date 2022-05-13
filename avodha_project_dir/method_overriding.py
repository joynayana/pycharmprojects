class A:
    def show(self):
        print("in A")
class B(A):
    pass
b1=B()
b1.show()