n=eval(input())
l=[]
for i in range(n+1):
    x=2
    y=1
    a=x/y
    y=x
    x=x+y
    l.append(a)
s=sum(l)
print("%.4f"%s)
