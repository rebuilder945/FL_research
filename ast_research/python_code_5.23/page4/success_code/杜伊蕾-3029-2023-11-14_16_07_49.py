a=input().split(',')
a=list(a)
b=eval(input())
d=[]
for x in range(len(a)):
    c=[]
    c.append(a[x])
    c.append(b[x])
    d.append(c)
print(d)

