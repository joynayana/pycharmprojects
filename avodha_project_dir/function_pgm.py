def addition(a,b):
    c=a+b
    print("sum=",c)
addition(35,45)
# return statement
def multiply(x,y):
    z=x*y
    return z
print(multiply(30,5))
# arguments
def my_function(fname):
    print(fname+" "+"tomy")
my_function("neha")
my_function("raju")
my_function("roy")
# arbitary arguments(dont know howmany arguments)
def play_school(*kids):
     print(kids)
play_school("ram","ema","emm","reena")
keyword argument(key->value)
def record(name1,name2):
   print(name2)
record(name1="anna",name2="renne")
# arbitary keyword arguments(donot know how many keyword argument is passing)
def employee(**members):
   print(members["lastname"])
employee(fname="rahul",lastname="ravi")
# default parameter value
def sub_function(q=10,w=20):
    print(q+w)
sub_function(10,5)
sub_function()#function call without argument
# passing a list as an argument
def arg_function(color):
    for x in color:
        print(x)
flower=["rose","jasmin","bogun","cbcn"]
arg_function(flower)

