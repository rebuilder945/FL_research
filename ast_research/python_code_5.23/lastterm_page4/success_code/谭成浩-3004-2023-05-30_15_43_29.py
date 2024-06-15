def zhishu(m):
    fi=int(m**(1/2))+1
    if m==1:
        return 0
    else:
        for i in range(2,fi):
            if m%i==0:
                return 0
            return 1
date=eval(input())
n=[]
for x in date:
    if zhishu(x)==1:
        n.append(x)
print(n)
