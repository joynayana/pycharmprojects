# list in python
list1=["cow","dog","cat","bird"]
# print(list1)
# print(list1[3])
# print(list1[-1])
# print(list1[1:3])
# print(list1[:3])
# print(list1[1:])
# list1[1:3]=["tiger","lion","bear"]
# print(list1)
# list1[1:3]=["deer"]
# print(list1)
# print(type(list1))
# list2=[1,2,5,6]
# print(list2)
# print(list1+list2)
# a=["nayana",234,20.6,2j,"hai"]
# print(a)
# print("cow" in list1)
# print(3 in list2)
# list1.append("tiger")
# print(list1)
# list1.insert(0,"fish")
# print(list1)
# print(len(list1))
# print(list1.index("dog"))
# list constructor
a=list(("pen","book","orange","text","mouse","phone","laptop"))
print(a)
a.remove("pen")
print(a)
a.pop()#remove last item
print(a)
del a[0]
print(a)
# clear method clear entire list
a.clear()
print(a)
a=list(("pen","book","orange","text","mouse","phone","laptop","pen"))
a.sort()
print(a)
a.reverse()
print(a)
mylist=a.copy()
print(mylist)
x=a.count("pen")
print(x)




