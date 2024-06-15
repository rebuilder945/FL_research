def sspd(f):
    pd=True
    if f==1 or f==0:
        pd=False
    for j in range(1,int(f**0.5)+1):
        if f%j==0:
            pd=False
            break
    return pd
ss=eval(input())
print(ss)
ss1=[]
for i in ss:
    if sspd(i):
        ss1.append(i)
print(ss1)
