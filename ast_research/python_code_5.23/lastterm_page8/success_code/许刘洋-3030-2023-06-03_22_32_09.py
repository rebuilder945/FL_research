a=list(input().split(','))
b=list(input().split(','))
c=[]
for i in range(len(a)):
    c.append(a[i],b[i])
d=[]
d.append(c)
d.sort(key=b)
print(d)
