#function that handles divide by zero exception
def divide_function(a,b):
    try:
        c=a/b
        print(c)
    except ZeroDivisionError as e:
        print("Error-",e)
x=int(input("Enter two numbers:"))
y=int(input(""))
divide_function(x,y)
