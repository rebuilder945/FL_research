n=eval(input())
l=[]
for i in range(n+1):
    x=2
    y=1
    a=x/y
    m=y
    y=x
    x=x+m
    l.append(a)
s=sum(l)
print("%.4f"%s)
