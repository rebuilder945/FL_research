def zhishu(m):
    if m==1:
        return 0
    elif m==2:
        return 1
    else:
        for i in range(2,m):
            if m%i==0:
                return 0
            return 1
date=eval(input())
n=[]
for x in date:
    if zhishu(x)==1:
        n.append(x)
print(n)
