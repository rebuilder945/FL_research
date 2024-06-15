a=list(eval(input()))
n,m=int(input())
d=[]
if (n+1)<=len(a):
    for i in range(m):
        d.append(a[n])
    a=a+d
    print(a)
else:
    print('error')
