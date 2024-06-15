a=input().split(',')
b=eval(input().split(','))
c=[]
d=[]
for x in range(len(a)):
    c.append(a[x])
    c.append(b[x])
    d.append(c)
    c=[]
print(d)

