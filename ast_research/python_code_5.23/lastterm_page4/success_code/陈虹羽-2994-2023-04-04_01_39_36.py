a=list(eval(input()))
n,m=eval(input())
c=len(a)
if n>=0:
    if n in range(c):
        d=a[n]
        
        for i in range(m):
            a.append(d)
        print(a)
    else:
        print('error')
else:
    if n+c in range(c):
        d=a[n]
        
        for i in range(m):
            a.append(d)
        print(a)


