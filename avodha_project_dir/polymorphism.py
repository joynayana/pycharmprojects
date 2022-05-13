#polymorphism-duck typing
class maths:
    def exicute(self):
        print("equation")
class selection:
    def choose(self,subject):
        subject.exicute()
subject=maths()
s1=selection()
s1.choose(subject)