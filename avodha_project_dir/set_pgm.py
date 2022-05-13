# unordered and indexed
set1={"a","b","c","d"}
# print(set1)
# print(type(set1))
# print(len(set1))
# for i in set1:
#     print(i)
# print("c" in set1)
# # add element to set
# set1.add("e")
# print(set1)
# # remove item
# set1.remove("e")
# print(set1)
# set1.discard("d")
# print(set1)
# # remove last
# set1.pop()
# print(set1)
# set1.clear()
# print(set1)
# del set1
# print(set1)
#set constructor
# a=set((1,2,3,3,4,5))
# print(a)
x={1,2,3,4,5,6}
y={3,4,5,6,7,8}
# different union method
d=x.union(y)
print(d)
# g=x|y
# print(g)
# x.update(y)
# print(x)
print('intersection')
s=x-y
print(s)
# s=y-x
# print(s)
# s=x.difference(y)
# print(s)
#list is sorted by converting set
lis=[1,7,3,8,2,1,6]
sort=set(lis)
print(type(sort))
print(sort)
print('----------')
lis={1,7,3,8,2,1,6}
t=sorted(lis)
print(t)
print(type(t))
print((t[::-1]))

