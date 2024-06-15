a=input().split(',')
b=input().split(',')
for  x  in  range(len(b)):
    a[x]=eval(a[x])
c=[]
d=[]
for x in range(len(a)):
    c.append(a[x])
    c.append(b[x])
    d.append(c)
    c=[]
print(d)

