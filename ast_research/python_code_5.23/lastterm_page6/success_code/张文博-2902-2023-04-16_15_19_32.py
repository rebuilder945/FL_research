m=eval(input())
a=[1,1]
for x in range(m+3):
    b=0
    b=a[x]+a[x+1]
    a.append(b)
b=[]
for x in range(m):
    c=a[x+2]/a[x+1]
    b.append(c)
s=sum(b[:m])

print("%.4f"%s)

