a=input().split(" ")
b={}
c=0
for i in a:
    b[i]=b.get(i,0)+1
    if b[i]>c:
        c=b[i]
d=[]
for i,j in b.items():
    if j==c:
        d.append(i)
for i in d:
    print(i,c)
