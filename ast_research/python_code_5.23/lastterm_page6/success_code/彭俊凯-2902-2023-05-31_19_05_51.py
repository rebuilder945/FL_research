def l(c):
    d=[1,1]
    for i in range(c):
        a=d[i]+d[i+1]
        d.append(a)
    return d[c+1]
b=[]
x=eval(input())
for i in range(x):
    o=l(i+1)/l(i)
    b.append(o)
n=sum(b)
print('%.4f'%(n))

