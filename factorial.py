#Factorial Number
n= int(input("enter factorial no."))
for i in range(1, n):
    n= n*i
    i+=1
print(n)

#using Function
n = int(input("enter fact no."))
def fact(n):
    for i in range(1, n):
        n = n * i
        i = i + 1
    print(n)

fact(n)


#Using Recursion

import sys
sys.setrecursionlimit(5000)  #increase the recursion limmit
print(sys.getrecursionlimit()) #get recursion limit (default is 1000)

#Factorial number using Recursion

n=int(input("enter factorial no."))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result =fact(n)
print(result)
