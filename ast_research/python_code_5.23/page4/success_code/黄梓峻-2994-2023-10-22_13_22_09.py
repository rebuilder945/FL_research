import math
def hou(y,n,m):
    if n!=math.floor(n):
        return
        print('error')
    else:
        if n>=(-len(y)) and n<len(y):
            x=y[n]
            for i in range(m):
                y.append(x)
            return
            print(k)
        else:
            return
            print('error')
        
sums=list(eval(input()))
n,m=eval(input())
k=hou(sums,n,m)
print(k)
