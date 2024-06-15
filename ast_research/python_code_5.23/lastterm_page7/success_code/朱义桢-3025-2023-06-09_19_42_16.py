a=input().split()
b={}
for x in a:
    b[x]=b.get(x,0)+1
c=[]
for k,v in b.items():
    c.append([k,v])
c.sort(key=lambda x:x[1],reverse=True)
m=c[0][1]
for x in c:
    if x[1]==m:
        print(x[0],x[1])
