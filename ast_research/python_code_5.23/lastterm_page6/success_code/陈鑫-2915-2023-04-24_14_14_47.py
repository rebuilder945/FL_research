
a=eval(input())

b=str(a)
c=[]
d=0
for i in range(len(b)):
    c.append(b[i])
for i in range(len(c)):
    d+=int(c[i])**3
print(d)
