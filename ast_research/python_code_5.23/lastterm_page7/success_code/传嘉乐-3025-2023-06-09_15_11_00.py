a=input().split()
b={}
c=[]
for x in a:
    b[x]=b.get(x,0)+1
for k,v in b.items():
    c.append([k,v])
c.sort(key=lambda x:x[0],reverse=False)
c.sort(key=lambda x:x[1],reverse=True)
for i in range(len(c)):
    if c[i][1]==c[0][1]:
        print(c[i][0],c[i][1])

