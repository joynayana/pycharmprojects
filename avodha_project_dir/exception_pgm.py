# exception handling in divion by zero
# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("sorry. you cannot divide by zero")
# finally:
#     print("finally")
# # exception handling out of index in list
# try:
#     list1=[1,2,3,4,5]
#     print(list1[5])
# except:
#     print("invalid index")
# #exception based on object
# try
#     a=10
#     b=0
#     print(a/b)
# except Exception as e:
#     print("sorry. you cannot divide by zero",e)
# finally:
#     print("finally")
#multiple exception handle
try:
    a=int(input("enter a number:"))
    b=2
    print(a/b)
    print(hai)
except ZeroDivisionError as e:
    print("sorry.",e)
except ValueError as e:
    print("sorry",e)
except Exception as e:
    print("sorry",e)
finally:
    print("finally")

