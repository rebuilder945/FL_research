n,m=tuple(input().split(' '))
n=int(n)
m=int(m)
lst=[]
if 0<=n<=(m-3):
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a:
                    lst.append(a*100+b*10+c)
    result=[]
    for x in lst:
        if 0<(x//100)<10:
            result.append(x)
    print(' '.join(list(map(str,result))))
else: print('illegal input')
