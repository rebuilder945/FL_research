b=[]
while True:
    a=input() or "q"
    if a=="q":
        break
    b.append(a)
c={}
for x in b:
    c[x]=0
for x in b:
    c[x]+=1
d=[]
for k,v in c.items():
    d.append([k,v])
d.sort(key=lambda x:x[1],reverse=True)
print(d[0][0],d[0][1])
