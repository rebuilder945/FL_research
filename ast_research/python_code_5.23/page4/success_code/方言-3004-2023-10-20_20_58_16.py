def sspd(i):
    pd=True
    for j in range(int(i**0.5)):
        if i%j==0:
            pd=False
    return pd


ss=eval(input())
ss1=[]
for i in ss:
    if sspd(i):
        ss1.append(i)
print(ss1)
