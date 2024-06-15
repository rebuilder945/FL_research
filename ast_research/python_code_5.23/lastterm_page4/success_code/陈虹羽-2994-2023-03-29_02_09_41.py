a=list(input().split(','))
n,m=eval(input())
c=len(a)
if n+1 not in range(c):
    print('error')
else:
    c=[a[n]]
    
    d=a+c*m
    f=[int(i)for i in d ]
    print(f)
    
