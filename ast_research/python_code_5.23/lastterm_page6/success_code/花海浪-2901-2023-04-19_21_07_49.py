a=""
b=[]
while a!="#":
    a=(input(""))
    b.append(a)
del b[-1]
e=[]
for x in b:
    x=int(x)
    e.append(x)
c=len(e)
f=sum(e)
print("%d %d"%(c,f))

