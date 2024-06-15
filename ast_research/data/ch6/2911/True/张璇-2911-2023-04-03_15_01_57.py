a=list(input())
c=[]
for x in range(len(a)):
    b=(int(a[x])+5)%10
    c.append(b)
c[0],c[-1]=c[-1],c[0]
if len(c)>2:
    c[1],c[-2]=c[-2],c[1]
d=[]
for i in range(len(c)):
    n=str(c[i])
    d.append(n)
f="".join(d)
print(f)
