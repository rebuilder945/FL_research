a=eval(input())
lt=list(a)
n,m=eval(input())
l=len(lt)
if -l<=n<=l-1:
    t=a[n]
    ls=[t]
    ii=ls*m
    z=lt+ii
    print(z)
else:
    print("error")
