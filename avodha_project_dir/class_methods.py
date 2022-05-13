class student:
    school="greatbatch"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    # class method
    @classmethod
    def get_shool(cls):
        return cls.school
    # static method
    @staticmethod
    def info():
        print("its a static method not belongs to any object")
    # def set_m1(self):
    #     self.m1=38
    # def get_m1(self):
    #     return self.m1
s1=student(45,47,34)
s2=student(34,34,45)
print(s1.avg())
print(s2.avg())
print(student.get_shool())
student.info()
# s1.set_m1()
# print(s1.get_m1())