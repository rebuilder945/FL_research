a=input().split()
b={}
for x in a:
    b[x]=b.get(x,0)+1
c=[]
d=[]
for k,v in b.items():
    c.append([k,v])
    d.append(v)
m=max(d)
n=d.count(m)
c.sort(key=lambda x:x[1],reverse=True)
for i in range(n):
    print(c[i][0],c[i][1])
