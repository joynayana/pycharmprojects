class family:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
             return False
f1=family("nayana",23)
f2=family("kunju",7)
f1.display()
f2.display()
if f1.compare(f2):
    print("there are equal")
else:
    print("there are not equal")