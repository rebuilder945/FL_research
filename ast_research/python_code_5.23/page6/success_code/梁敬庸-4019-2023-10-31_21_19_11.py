b=list(input())
a=len(b)
for x in range(a):
    c=int(b[x])+5
    d=c%10
    b.append(d)

del b[0:a]
f=int(a/2)
for i in range(f):
    b[i],b[-1-i]=b[-1-i],b[i]


sum=""
for h in b:
    h=str(h)
    sum+=h
print(sum)
