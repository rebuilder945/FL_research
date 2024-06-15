a=list(map(int.input().split(',')))
n,m=eval(input())
b=[]
if(n+1)<=len(a):
    for x in range(m):
        b.append(a[n])
    a=a+b
    print(a)
else:
    print('error')
