def isPrime(n):
    if n>2:
        for i in range(2,n):
            if n%i==0:
                return 0
    return 1
def reversenumber(n):
    num=str(n)
    m=num[::-1]
    if m==num:
        return n
n=float(input())
if n-int(n)>0:
    print("illegal input")
elif int(n)<1:
    print("illegal inpput")
else:
    n=int(n)
    s=[]
    for x in range(2,n):
        if isPrime(x) and reversenumber(x)==x:
            s.append(x)
    for x in range(len(s)):
        print("%d"%s[x],end='')

