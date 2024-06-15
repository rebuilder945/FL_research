def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return 0
    else:
        return 1
def revnum(n):
    num=str(n)
    if num[::-1]==num:
        return n
N=float(input())
if (N-int(N))>0:
    print("illegal input")
elif int(N)<=1:
    print('illegal input')
else:
    N=int(N)
    n=[]
    m=2
    for x in range(2,N):
        if isprime(x) and revnum(x)==x:
            n.append(x)
        for x in range(len(n)):
            print('%d'%n[x],end='')

