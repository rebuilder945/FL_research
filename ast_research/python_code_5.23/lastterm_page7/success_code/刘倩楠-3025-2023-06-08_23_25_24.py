s=list(input().split(" "))
p=s.sort(reverse=False)
a={}
for x in p:
    a[x]=p.count(x)
lt=[]
ls=[]
for k,v in a.items():
    lt.append([k,v])
    ls.append(int(v))
b=[]
for y in lt:
    if y[1]==max(ls):
        b.append(y)
for x in c:
    for y in x:
        print(y,end=" ")
    print()

