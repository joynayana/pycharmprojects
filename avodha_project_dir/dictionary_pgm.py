fruit={"apple":100,"orange":200,"pinapple":400,"mango":500}
print(fruit)
print(fruit["apple"])
# to change value
fruit["mango"]=600
print(fruit)
# to print key
for x in fruit:
      print(x)
# to print value
for i in fruit:
    print(fruit[i])
# to list all keys
for x in fruit.keys():
    print(x)
# to print values
for i in fruit.values():
    print(i)
# to print key and values
for x,y in fruit.items():
    print(x,y)
# copy a dictionary items
mydict=fruit.copy()
print(mydict)
# copy using dict function
newdict=dict(fruit)
print(newdict)