x=2
y=1
n=eval(input())
l=[]
for i in range(n):
    a=x/y
    m=y
    y=x
    x=x+m
    l.append(a)
s=sum(l)
print("%.4f"%s)
