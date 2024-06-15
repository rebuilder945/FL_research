a= input()
b = a[1:-1]
c = b.split(',')
c.reverse()
d=[]
e=[]
for x in c:
    if not x in d:
        d.append(x)
        continue
d.reverse()
print(d)
