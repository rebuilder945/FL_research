import math
def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return 0
            return 1
def reversenumber(m):
    num=str(m)
    m=num[::-1]
    if num==m:
        return m
s=float(input())
if (s-int(s))>0:
    print("illegal input")
if int(s)<1:
    print("illegal input")
else:
    s=int(s)
    h=[]
    for x in range(2,s):
       if isprime(x)and reversenumber(x)==x:
          h.append(x)
    for x in range(len(h)):
          print("%d"%h[x],end='')
    
