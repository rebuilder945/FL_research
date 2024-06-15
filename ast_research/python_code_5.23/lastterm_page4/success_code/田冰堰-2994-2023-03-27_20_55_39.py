ls=eval(input())
n,m=eval(input())
a=len(ls)
if n>=a:
    print("error")
else:
    for i in range(a):
        if i==n:
            b=ls[i]
    ls1=([b]*m)
    print(ls+ls1)
