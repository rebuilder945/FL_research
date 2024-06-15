def zhishu(m):
    i=2
    while i<=m**(1/2):
        if m%i==0:
            return 0
        i+=1
        return 1
date=eval(input())
n=[]
for x in date:
    if zhishu(x)==1:
        n.append(x)
print(n)
