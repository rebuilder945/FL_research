a=list(str(input()))
b=eval(input())
c=[]
d=[]
for i in range(3):
    c.append(a[i])
    c.append(b[i])
    d.extend(c)
print(d)

