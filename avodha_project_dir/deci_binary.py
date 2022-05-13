# fibonacci series
# x=int(input("enter the limit:"))
# num1=0
# num2=1
# print(num1,num2,end=' ')
# count=2
# while count!=x:
#     sum=num1+num2
#     num1=num2
#     num2=sum
#     print(sum,end=' ')
#     count+=1
# # average of integers
# limit=int(input("enter the limit:"))
# print("enter the integers:")
# sum=0
# for i in range(limit):
#    x=int(input())
#    sum=sum+x
# avg=sum/limit
# print("avg:",avg)
# # area of a circle
# import math
# r=int(input("enter radius of a circle:"))
# area=math.pi*r*r
# print(area)
# # print reverse of a digit
# num=int(input("enter a + ve integer:"))
# rev=0
# while num!=0:
#     r=num%10
#     rev=r+(rev*10)
#     num=num//10
# print(rev)
# print sum of digit in a number
# num=int(input("enter a + ve integer:"))
# sum=0
# while(num!=0):
#     rem=num%10
#     sum+=rem
#     num=num//10
# print(sum)
# # checking prime number
# n=int(input("enter a + ve integer:"))
# prime=1
# if n==2:
#     print("prime")
# for i in range(2,n-1):
#      if n % i==0:
#          prime=0
#          break
# if prime==1:
#     print("prime")
# else:
#     print(" not prime")
## prime numbers in between numbers
# n=10
# for i in range(1,n+1):
#     if i>1:
#         for j in range(2,i):
#             if (i%j)==0:
#                 break
#         else:
#             print(i)
# # print n to 1
# n=int(input("enter a number:"))
# for i in range(n,0,-1):
#     print(i)
# n to 1 using recursion
# def fun(n):
#     if n==0:
#         return
#     print(n)
#     n=n-1
#     fun(n)
# fun(10)


