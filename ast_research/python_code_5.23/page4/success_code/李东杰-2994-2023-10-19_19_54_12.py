a=list(eval(input()))
n,m=eval(input())
d=len(a)
if n>=0 and n in range(d):

    b=[a[n]]
    c=b*m
    a.extend(c)
    print(a)
elif -n in range(d):
    b=[a[n]]
    c=b*m
    a.extend(c)
    print(a)
else:
    print("error")

