from math import*
def isprime(n):
    for j in range(2,int(sqrt(n))+1):
        if n%j==0:
            return 0
    return 1

def ishui(n):
    n1=n[::-1]
    
    if n1==n:
        return 1
    return 0
    
x=int(input())
i=0
n=2
while(i<x):
    if(isprime(n) and ishui(str(n))):
        print(n,end=' ')
        i+=1
    n+=1
