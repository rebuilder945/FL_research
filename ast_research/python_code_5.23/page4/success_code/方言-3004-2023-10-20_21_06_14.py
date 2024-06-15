def sspd(f):
    pd=True
    for j in range(1,int(f**0.5)):
        if f%j==0:
            pd=False
    return pd
ss=eval(input())
print(ss)
ss1=[]
for i in ss:
    if sspd(i):
        ss1.append(i)
print(ss1)
