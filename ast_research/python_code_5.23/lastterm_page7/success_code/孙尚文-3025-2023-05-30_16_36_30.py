a=input().split()
b={}
for i in a:
    b[i]=b.get(i,0)+1
c=[]
for k,v in b.items():
    c.append([k,v])
c.sort(key=lambda x:x[1],reverse=True)
d=c[0][0]
e=c[0][1]
print(c)

print("{} {}".format(d,e))


