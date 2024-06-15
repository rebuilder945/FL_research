x=list(map(int(float,input().split())))
n,m=eval(input())
b=[]
if n<=(len(x)-1):
    for i in range(m):
        b.append(x[n])
    x=x+b
    print(x)
else:
    print('error')
