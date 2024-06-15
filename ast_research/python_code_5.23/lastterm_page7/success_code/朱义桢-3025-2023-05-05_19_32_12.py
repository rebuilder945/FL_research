a=input().split()
b={}
for x in a:
    b[x]=b.get(x,0)+1
b=dict(sorted(b.items()))
c=[]
d=[]
for k,v in b.items():
    c.append([k,v])
    d.append(v)
m=max(d)
n=d.count(m)
c.sort(key=lambda x:x[1],reverse=True)
x=[]
for i in range(n):
    x.append(c[i])
for i in x:
    print(i[0],i[1])
