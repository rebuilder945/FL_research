def zhi(x):
    if x>1:
        for i in range(2,x):
            if x%i==0:
                return 0
    return 1
def hui(x):
    n=str(x)
    m=n[::-1]
    if n==m:
        return 1
    else:
        return 0
a=float(input())
if a!=int(a) or a<1:
    print('illegal input')
else:
    a=int(a)
    hwss=[]
    for i in range(2,a):
        if zhi(i)==1 and hui(i)==1:
            hwss.append(i)
    for i in range(len(hwss)):
        print("%d"%hwss[i],end=' ')



