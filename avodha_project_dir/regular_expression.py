import re
pattern=r"nayana"
# #match is used to find a pattern present in a given string in the beginning only
# if re.match(pattern,"nayana how are u"):
#     print("yes")
# else
#     print("not match")
if re.match(pattern,"hi how are you nayana"):
    print("nayana present at the beginning")
else:
    print("not present")
# search is used to find any pattern present any position in a given string
# s=r"welcome"
# n="hai welcome to the world of animals"
# if re.search(s,n):
#     print("present")
# else:
#     print("not present")
# findall return all pattern present in a string
# find=r"avodha"
# print(re.findall(find,"avodha is good avodha xcvv avodha avodha"))
# it replace another one
pattern=r"nayana"
str="hai nayana how are u.nayana hi.nayana"
new1=re.sub(pattern,"alvi",str)
print(new1)
# dot meta
pattern=r"th...ht"
if re.search(pattern,"my thought are wide"):
    print("yes")
else:
    print("not present")
# character class
pattern=r"^[b-z][A-Z][0-9]..play$"
if re.search(pattern,"bW4weplay"):
    print("ok")
else:
    print("not ok")