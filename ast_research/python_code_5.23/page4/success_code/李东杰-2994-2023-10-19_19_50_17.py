a=list(eval(input()))
n,m=eval(input())
d=len(a)
if n in range(d):

    b=[a[n]]
    c=b*m
    a.extend(c)
    print(a)
else:
    print("error")

