#oops in python
# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def getdata(self):
#         self.name=input("enter the name:")
#         self.mark=input("enter the mark:")
#     def displaydata(self):
#         print(self.name,self.mark)
# obj=student("","")
# obj.getdata()
# obj.displaydata()
# another type
# class data:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("hai my name is ",self.name,"and age is",self.age)
# obj1=data("nayana",20)
# obj1.display()
# nested class
# inner class's object is created in student class
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         # create object nested class
#         self.scolar=self.scolarship()
#     def display(self):
#         print(self.name,self.age)
#         self.scolar.display()
#     class scolarship:
#         def __init__(self):
#             self.mark=100
#             self.cash=4000
#         def display(self):
#             print(self.mark,self.cash)
# st1=student("nayana",26)
# st1.display()
# s=st1.scolar
# s.display()
# inner class's object is created outside
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fdisplay(self):
        print(self.name,self.age)
    class scolarship:
        def __init__(self):
            self.mark=100
            self.cash=4000
        def display(self):
            print(self.mark,self.cash)


st1=student('jerald',30)
sp=st1.scolarship()
sp.display()


