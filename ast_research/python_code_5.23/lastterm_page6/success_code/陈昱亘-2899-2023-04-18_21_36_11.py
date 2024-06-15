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
    result=lst.copy()
    for x in result:
        if x%100==x:
            lst.remove(x)
    print(' '.join(list(map(str,lst))))
else: print('illegal input')
