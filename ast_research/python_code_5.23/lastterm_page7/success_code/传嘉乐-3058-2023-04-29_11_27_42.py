a=input()
b={}
c=[]
while a != 'q':
    if a not in c:
        c.append(a)
        b[a]=1
    else:
        b[a]+=1
    a=input()
d=[]
for k,v in b.items():
    d.append([k,v])
d.sort(key=lambda x:x[1],reverse=True)
print(d[0][0],d[0][1])
