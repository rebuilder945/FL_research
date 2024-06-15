n=int(input())
c=[1,1]
for x in range(n):
    a=c[x]+c[x+1]
    c.append(a)
del c[0]
print(c)
d=[]
for x in range(n):
    e=c[x+1]/c[x]
    d.append(e)
    print(d)
d=sum(d)
print("%.4f"%(d))
