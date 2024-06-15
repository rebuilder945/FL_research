m=eval(input())
a=list(m)
b,c=eval(input())
d=abs(b)
e=len(a)
if d>=(e-1):
    print("error")
elif b<0:
    f=a[b]
    n=a[f]
    g=[n]*c
    print(a+g)
elif b>=0:
    f=a[b-1]
    n=a[f]
    g=[n]*c
    print(a+g)


