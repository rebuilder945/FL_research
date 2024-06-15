x=eval(input())
n,m=eval(input())
if 0<=n<=len(x)-1:
    b=x[n]*m
    x.append(b)
    print(x)
else:
    print('error')
