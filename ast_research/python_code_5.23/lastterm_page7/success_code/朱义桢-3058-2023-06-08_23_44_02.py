b=[]
while True:
    a=input()
    if a=="q":
        break
    b.append(a)
c={}
for x in b:
    d=c.get(x,0)+1
    c[x]=d
m=[]
for k,v in c.items():
    m.append([k,v])
m.sort(key=lambda x:x[1],reverse=True)
print(m[0][0],m[0][1])
