a=input().split()
b={}
for i in a:
    b[i]=b.get(i,0)+1
c=[]
for k,v in b.items():
    c.append([k,v])
c.sort(key=lambda x:x[1],reverse=True)
zuida=c[0][1]
lst=[]
for j in b:
    if b[j]==zuida:
        lst.append(j)
lst.sort()

for i in lst:
    print("{} {}".format(i,zuida))
