a=input().split(',')
b=input().split(',')
for  x  in  range(len(b)):
    b[x]=eval(b[x])
c=[]
d=[]
for x in range(len(a)):
    c.append(a[x])
    c.append(b[x])
    d.append(c)
    c=[]
d.sort(key=lambda x:x[1],reverse=True)
print(d)

