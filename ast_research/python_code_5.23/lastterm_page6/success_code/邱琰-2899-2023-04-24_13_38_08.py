n,m=map(eval,input().split())
if n<=m-3 and m<11 and n>=0:
    lst=[]
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a:
                    s=a*100+b*10+c
                    lst.append(s)
    print(*lst)
else:
    print('illsgal input')
