def fbnq(x):
    an=[1,1]
    for i in range(x):
        a=an[-1]+an[-2]
        an.append(a)
    return an
n=eval(input())
bn=[]
fn=fbnq(n+2)
for d in range(1,n+1):
    b=fn[d+1]/fn[d]
    bn.append(b)
s=sum(bn)
print('%.4f'%s)
