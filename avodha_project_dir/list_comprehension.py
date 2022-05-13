# def square():
#     for i in range(10):
#         print(i*i)
# square()
square=[i*i for i in range(10)]
print(square)
# letter=[]
# for i in "nayana":
#     letter.append(i)
# print(letter)
letter=[i for i in "nayana"]
print(letter)
# even=[]
# for i in range(10):
#     if i%2==0:
#         even.append(i)
# print(even)
even=[i for i in range(10) if i%2==0]
print(even)
power of even number in a list
li=[1,4,5,8]
pow=[i**2 for i in li if i%2==0]
print(pow)
v=[2,4,5]
l=[i*4 for i in v]
print(l)
a=[1,2,3,4]
b=[1,2,3,4]
cartition=[(x,y) for x in a for y in b]
print(cartition)