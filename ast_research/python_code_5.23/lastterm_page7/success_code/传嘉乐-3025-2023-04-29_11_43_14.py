a=input()
b={}
c=[]
d=''
for i in a:
    if i.isalpha():
        d+=i
    else:
        if d in c:
            b[d]+=1
        else:
            c.append(d)
            b[d]=1
            d=''
if d in c:
            b[d]+=1
else:
    c.append(d)
    b[d]=1
    d=''
e=[]
for k,v in b.items():
    e.append([k,v])
e.sort(key=lambda x:x[1],reverse=True)
print(e[0][0],e[0][1])

