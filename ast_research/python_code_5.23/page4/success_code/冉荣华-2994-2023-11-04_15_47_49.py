x=list(map(int,input().split()))
n,m=eval(input())
if n<=len(x)-1:
    b=[]
    for i in range(m):
        b.append(x[n])
    x=x+b
    print(x)
else:
    print('error')
