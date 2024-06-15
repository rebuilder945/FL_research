x=eval(input())
n,m=eval(input())
if 0<=n<=len(x)-1:
    b=[]
    for i in range(m):
        b.append(x[n])
        x.append(b)
    print(x)
else:
    print('error')
