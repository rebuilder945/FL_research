s=input().split()
a={}
b={}
for i in s:
    a[i]=a.get(i,0)+1
for x,y in a.items():
    if y == max(a.values()):
        b[x]=y
c=sorted(b)
for i in c:
    print(i,max(a.values()))

