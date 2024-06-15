a=input().split()
b={}
for x in a:
    if x not in b.keys():
        b[x]=1
    else:
        b[x]+=1
c=list(b.items())
c.sort(key=lambda x:x[0],reverse=True)
for x in c.keys():
    if c[x]==max(c.values()):
        print(x,c[x])
