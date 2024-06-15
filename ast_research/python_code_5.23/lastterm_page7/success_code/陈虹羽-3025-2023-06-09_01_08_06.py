a=input().split()
b={}
c=[]
d=0
for i in a:
    b[i]=b.get(i,0)+1
    if b[i]>d:
        d=b[i]

for k,v in b.items():
    if v==d:
        c.append([k,v])
c.sort()
for i in range(len(c)):
    m,n=c[i]
    print(m,n)

