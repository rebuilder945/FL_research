g={}
a=list(input().split())
for i in a:
    if i in g:
        g[i]+=1
    else:
        g[i]=1

b=0
k=[]
for i in g.values():
    if i>b:
        b=i
for j in g.keys():
    if g[j]==b:
        k.append(j)
k.sort()
for i in k:
    print(i,b)


