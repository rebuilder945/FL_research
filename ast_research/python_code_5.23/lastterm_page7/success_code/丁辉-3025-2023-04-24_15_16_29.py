a=input().split()
b={}
for x in a:
    if x not in b.keys():
        b[x]=1
    else:
        b[x]+=1
c=dict(sorted(b.items(),key=lambda x:x[0],reverse=True))
for x in c.keys():
    if c[x]==max(c.values()):
        print(x,c[x])
