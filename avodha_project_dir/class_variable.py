#type of variable in class 1) instant variable, 2) class variable(static variable)class family:
class family:
    familyname="arakal" #class variable
    def __init__(self,name,age):
        self.name=name #instance variable
        self.age=age
f1=family("nayana",23)
f2=family("kunju",7)
f1.familyname="velikal"
print(f1.name,f1.age,f1.familyname)
print(f1.name,f1.age,f1.familyname)
'''class variable can access any object. if one object change it value it will effect all the 
instances of class accessing that class variable'''