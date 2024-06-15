def isPrime(n):
    if n>0:
        for i in range(2,n):
            if n%i==0:
                return 0
        return 1
def reverseNumber(n):
    num=str(n)
    m=num[::-1]
    if m==num:
        return n
N=float(input())
if N-int(N)>0:
    print("illegal input")
elif int(N)<1:
    print("illegal input")
else:
    N=int(N)
    hui=[]
    for x in range(2,N):
        if isPrime(x) and reverseNumber(x)==x:
            hui.append(x)
for x in hui:
    print(x,end="")
