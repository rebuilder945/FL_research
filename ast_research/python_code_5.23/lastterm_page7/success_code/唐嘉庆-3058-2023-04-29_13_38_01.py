b=[]
c={}
while True:
    a=input()
    if a=='q':
        break
    else:
        b.append(a)
for i in b:
    if i in c:
        c[i]=c[i]+1
    else:
        c[i]=1
d=list(c.items())
d.sort(key=lambda x:x[1],reverse=True)
m,n=d[0]
print("{} {}".format(m,n))
