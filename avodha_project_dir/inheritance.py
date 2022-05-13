class student:
    def __init__(self,name,hodname):
        self.name=name
        self.hodname=hodname
    def setData(self):
        self.name=input("enter your name:")

class hod(student):
    def putData(self):
       self. hodname=input("enter hod name:")
    def getData(self):
        print("name of student:",self.name,"hod name:",self.hodname)
h1=hod('','')
h1.setData()
h1.putData()
h1.getData()

