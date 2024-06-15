a=input().split(sep=",")
s=input().split(sep=",")
l=len(a)
n=eval(s[0])
ii=[]
m=eval(s[-1])
if -l<=n<=-1 or 0<=n<=l-1:
    t=eval(a[n])
    t=[t]*m
    for x in a:
        x=eval(x)
        ii.append(x)
    zz=ii+t
    print(zz)
else:
    print("error")
