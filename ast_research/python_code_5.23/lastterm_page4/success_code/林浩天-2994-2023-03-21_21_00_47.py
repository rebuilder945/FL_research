import math
def mowei(y,n,m):
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
            
sums=list(eval(input()))
n,m=eval(input())
mowei(sums,n,m)

