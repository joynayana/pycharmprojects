#factorial of a number with out recursion
# def factorial(n):
#     fact=1
#     if n==1:
#         print(fact)
#     else:
#         for i in range(n,1,-1):
#             fact=fact*i
#         print(fact)
# factorial(5)
# with recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return (n * factorial(n-1))
n=5
print("factorial:",factorial(n))