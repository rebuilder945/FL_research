a=input().split(",")
b=input().split(",")
c={}
m=[]
for x in range(len(a)):
    c[a[x]]=eval(b[x])
d=dict(sorted(c.items(),key=lambda item:item[1]))

for k,v in d.items():
    n=[]
    n.append(k)
    n.append(v)
    m.append(n)
print(m)




        

