n,m=map(int,input().split())
if n+3<=m:
    for i in range(101,999):
        a=i%10
        b=(i//10)%10
        c=i//100
        if a!=b!=c!=a and a in range(n,m) and b in range(n,m) and c in range(n,m):
            print(i,end=' ')
elif n+3>m:
    print('illegal input')

