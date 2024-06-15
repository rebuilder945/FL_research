a=input() or "q"
b={}
while(a!="p"):
    b[a]=b.get(a,0)+1
    a=input() or "q"
c=[]
for k,v in b.items():
    c.append([k,v])
c.sort(key=lambda x:x[1],reserve=True)
print(c[0],c[0][1])
