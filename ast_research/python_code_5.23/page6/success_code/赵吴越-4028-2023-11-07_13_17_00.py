import math
def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return 0
    return 1
def reverseNumber(n):
    num=str(n)
    m=num[::-1]
    if num==m:
        return n 
N=eval(input())
if N<=1 or N%1!=0:
    print("illegal input")
else:
    N=int(N)
    hui=[]
    m=2
    for x in range(2,N):
        if isPrime(x) and reverseNumber(x)==x:
            hui.append(x)
    for x in range(len(hui)):
        print("%d"%hui[x],end=' ')




