class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3 = student(m1, m2)
        return s3
    def __gt__(self, other):
        if self.m1 > other.m1:
            return True
        else:
            return False
    def __str__(self):
       return '{} {}'.format(self.m1,self.m2)
s1=student(45,50)
s2=student(49,45)
s3=s1+s2
print(s3.m1,s3.m2)
if s1 > s2:
    print("grater")
else:
    print("lesser")
a=10
print(a)
# instead of getting address we wated to get value in s1 so operator override str method
print(s1)