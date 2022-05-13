# super class computer
class computer:
    def __init__(self,company,os):
        self.company=company
        self.os=os
    def getspecs(self):
        self.company=input("company name:")
        self.os=input("operating system:")
    def displayspecs(self):
        print("company:",self.company,"\noperating system:",self.os)
# sub classes laptop and desktop
class laptop(computer):
    def __init__(self,weight):
        self.weight=weight
    def setspecs(self):
        self.weight='2.5kg'
    def showspecs(self):
        print("Weight:",self.weight)
class desktop(computer):
    def __init__(self,monitor):
        self.monitor=monitor
    def takedata(self):
        self.monitor='lcd'
    def displaydata(self):
        print("monitor:",self.monitor)
# creating object of laptop
lap=laptop('')
lap.getspecs()
lap.displayspecs()
lap.setspecs()
lap.showspecs()
