from math import*
def First(n):
    for j in range(2,int(sqrt(n))+1):
        if n%j==0:
            return 0
def Second(n):
    n1=n[::-1]

    if n1==n:
        return 1
    return 0
x=int(input())
i=0
n=2
while(i<x):
    if (First(n) and Second(str(n))):
        print(n,end="")
    n+=1

if n==float or n<0:
    print("illegal input")
