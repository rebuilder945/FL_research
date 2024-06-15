a=list(input())
b=eval(input())
c=[]
d=[]
for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])
    d.extend(c)
print(d)

