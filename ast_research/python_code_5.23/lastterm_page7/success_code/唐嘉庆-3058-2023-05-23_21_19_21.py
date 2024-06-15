b=[]
c={}
while True:
    a=input()
    if a=='q':
        break
    else:
        b.append(a)
for i in b:
    b[i]=b.get[i,0]+1
print(b)
print(c)
d=list(c.items())
print(d)
d.sort(key=lambda x:x[1],reverse=True)
print(d)
m,n=d[0]
print("{} {}".format(m,n))
