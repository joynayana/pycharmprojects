class school:
    def __init__(self,schoolname):
        self.schoolname=schoolname
    def display1(self):
        self.schoolname=input("enter school name:")
class student:
    def __init__(self,name):
        self.name=name
    def display2(self):
        self.name=input("enter student name:")
class mark(school,student):
    def __init__(self,mark):
        self.mark=mark
    def display3(self):
        self.mark=input("enter mark:")
        print("schoolname:",self.schoolname)
        print("name:", self.name)
        print("mark:",self.mark)

obj=mark('')
obj.display1()
obj.display2()
obj.display3()



