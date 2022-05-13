# format method format specified value and place them inside the string palceholder
# list=[10,20,30,40]
# newstring="numbers:{0},{2},{3}".format(list[0],list[1],list[2],list[3])
# print(newstring)
# price=38
# txt="price {} in dollars".format(price)
# print(txt)
# price=49
# txt="price {:.2f} in dollars"
# print(txt.format(price))
# txt="price is:{price}".format(price=34)
# print(txt)
# fname="alen"
# lname="mathew"
# age="23"
# data="His name is {0} {1} and his father name is {1} age is{2}".format(fname,lname,age)
# print(data)
data="His name is {fname} {lname} and his father name is {lname} age is{age}".format(fname="mia",lname="john",age=34)
print(data)
fname="jeltin"
lname="george"
age="29"
data="His name is {} {} and his age is{}".format(fname,lname,age)
print(data)
