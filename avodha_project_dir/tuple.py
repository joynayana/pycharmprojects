a=("car","bike","cycle","van")
# print(a)
# print(a[0])
# print(len(a))
# print(type(a))
# print(a[1:4])
# for i in a:
#     print(i)
# if "cycle" in a:
#     print("yes present")
# to add item to tuple
t1=(1,2,3,2,4,5,6,2)
y=list(t1)
y[5]=7
t1=tuple(y)
print(t1)
# to check count of a element
print(y.count(2))
# tuple join
x=t1+a
print(x)
# unpacking tuple
(red,green,*blue)=a
print(red)
print(green)
print(blue)
#del a tuple
del a
print(a)