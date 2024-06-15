n=eval(input())
a=[2,3]
b=[1,2]
for x in range(n):
    if x >1:
        d=a[x-1]+a[x-2]
        e=b[x-1]+b[x-2]
        a.append(d)
        b.append(e)
nmsl=[]
for x in range(n):
    f=a[x]/b[x]
    nmsl.append(f)
c=0
for x in nmsl:
    c=c+x
print("%.4f"%c)
