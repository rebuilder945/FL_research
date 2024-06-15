b=[]
c={}
while True:
    a=input()
    if a=='q':
        break
    else:
        b.append(a)
for i in b:
    c[i]=c.get[i,0]+1
d=list(c.items())
d.sort(key=lambda x:x[1],reverse=True)
m,n=d[0]
print("{} {}".format(m,n))
