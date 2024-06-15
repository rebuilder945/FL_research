a=input().split()
b={}
for i in a:
    b[i]=b.get(i,0)+1
c=max(b.values())
d=list(b)
for i in d:
    if b[i]==c:
        print(i,c)
