import math
def hou(y,n,m):
    if n!=math.floor(n):
        print('error')
    else:
        if n>=(-len(y)) and n<len(y):
            x=y[n]
            for i in range(m):
                y.append(x)
            print(y)
        else:
            print('error')
    return(hou(y,n,m))
        
sums=list(eval(input()))
n,m=eval(input())
k=hou(sums,n,m)
print(k)
