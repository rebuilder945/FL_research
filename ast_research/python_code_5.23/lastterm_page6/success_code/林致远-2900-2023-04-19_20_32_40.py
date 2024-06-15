import math
def a(n):
    if n > 1:
        for x in range(2,n):
            if n%x==0:
                return 0
    return 1
def b(n):
    num = str(n)
    m = num[::-1]
    if num == m:
        return n
N = float(input())
if (N-int(N))>0:
    print('illegal input')
elif int(N)<1:
    print('illegal input')
else:
    N=int(N)
    h=[]
    m=2
    for x in range(2,N):
        if a(x) and b(x)==x:
            h.append(x)
    for x in range(len(h)):
        print('%d ' % h[x],end='')
