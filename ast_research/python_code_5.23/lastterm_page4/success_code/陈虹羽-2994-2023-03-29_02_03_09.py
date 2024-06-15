a=list(input().split(','))
n,m=eval(input())
c=len(a)
if n+1 not in range(c):
    print('error')
else:
    c=a[n]
    e=[str(i)for i in c]
    d=a+e*m
    f=[int(i)for i in d ]
    print(f)
    
