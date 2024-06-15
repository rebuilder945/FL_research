a=input().split()
b={}
c=0
for i in a:
    b[i]=b.get(i,0)+1
    if b[i]>c:
        c=b[i]
m=[]
for k,v in b.items():
    if v==c:
        m.append([k,v])
m.sort()
for k,v in m:
    print(k,v)

