import math
def sushu(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
    return True
def huiwenshu(n):
    c=str(n)
    m=c[::-1]
    if c==m:
        return n
n=eval(input())
if (n-int(n))>0:
    print("illegal input")
elif int(n)<1:
    print("illegal input")
else:
    q=int(n)
    huiwensushu=[]
    for i in range(2,q+1):
        if i==huiwenshu(n) and i==sushu(n):
            huiwensushu.append(i)
    for x in range(len(huiwensushu)):
        print("%d"%huiwensushu[x],end=' ')


