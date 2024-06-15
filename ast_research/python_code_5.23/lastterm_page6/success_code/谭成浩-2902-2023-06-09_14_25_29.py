def shu(m):
    x1=1
    x2=1
    x3=0
    if m==1:
        return x1
    for i in range(m-1):
        x3=x1+x2
        x1=x2
        x2=x3
    return x3
n=eval(input())
x=[]
for i in range(n):
    g=shu(i+2)/shu(i+1)
    x.append(g)
print('%.4f'%(sum(x)))
