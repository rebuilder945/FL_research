a=input().split()
b={}
c=0
for i in a:
    b[i]=b.get(i,0)+1
    if b[i]>c:
        c=b[i]
d=[]
for m,n in b.items():
    if n==c:
        d.append([m,n])
d.sort()
for m,n in d:
    print(m,n)
