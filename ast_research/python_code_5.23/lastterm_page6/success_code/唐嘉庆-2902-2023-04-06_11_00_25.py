n=eval(input())
a=[2]
b=[1]
for i in range(n):
    c=a[i]+b[i]
    a.append(c)
    b.append(a[i])
d=[]
for i in range(n):
    x=a[i]/b[i]
    d.append(x)
e=sum(d)
print('%.4f'%(e))
