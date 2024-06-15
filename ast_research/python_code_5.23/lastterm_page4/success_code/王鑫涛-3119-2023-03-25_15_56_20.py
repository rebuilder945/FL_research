a= eval(input())
c= list(a)
c.reverse()
d=[]
e=[]
for x in c:
    if not x in d:
        d.append(x)
        continue
d.reverse()
print(d)
