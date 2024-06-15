a=input()
b=[]
b.append(a)
while(a !="q"):
    a=input()
    b.append(a)
b.pop()
c={}
for i in b:
    if i in c:
        c[i]=c[i]+1
    else:
        c[i]=1
d=list(c.items())
d.sort(key=lambda x:x[1],reverse=Ture)
m,n=d[0]
print("{} {}".format(m,n))
