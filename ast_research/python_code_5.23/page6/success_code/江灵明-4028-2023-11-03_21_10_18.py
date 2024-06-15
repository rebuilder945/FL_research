import math
def isprime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
               return n
    else:
        return 1
def reversenumber(n):
    a = str(n)
    b = a[::-1]
    if b==a:
        return n
N = float(input())
if (N-int(N))<1:
    print("illegal input")
elif int(N)<1:
    print("illegal input")
else:
    N=int(N)
    h = []
    m = 2
    for x in range(2,N):
        if isprime(x) and reversenumber(x) ==x:
            h.append(x)
    for x in range(len(h)):
        print("%d"%h,end='')
