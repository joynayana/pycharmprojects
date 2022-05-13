''' Method overloading means same method with diffrent parameters .In python
 a method no supported.To implementing this we use none keyword.
'''
class student:
    def __init__(self):
        pass
    def sum(self,a=None,b=None,c=None):
       s=0
       if a!=None and b!=None and c!=None:
           s=a+b+c
       elif a!=None and b!=None:
           s=a+b
       else:
           s=a
       return s
s1=student()
print(s1.sum(20,30))
# a=None,b=None,c=None