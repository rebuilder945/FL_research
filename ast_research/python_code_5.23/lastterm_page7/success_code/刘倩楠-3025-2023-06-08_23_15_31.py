s=list(input().split(" "))
a={}
for x in s:
    a[x]=s.count(x)
lt=[]
ls=[]
for k,v in a.items():
    lt.append([k,v])
    ls.append(int(v))
b=[]
for y in lt:
    if y[1]==max(ls):
        b.append(y)
b=b.sort(reverse=True)
for x in b:
    for y in x:
        print(y,end=" ")
    print()

