m=input().split()
c={}
o=[]
for x in m:
    if c.get(x)==None:
        c[x]=1
    else:
        c[x]+=1
k=max(c.keys(),key=(lambda x:c[x]))
for x in c:
    if c[x]==c[k]:
        print(x,c[x])



