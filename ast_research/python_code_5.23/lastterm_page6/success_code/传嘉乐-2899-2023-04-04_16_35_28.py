n,m=map(int,input().split())
if 0<=n<m<11 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b!=c!=a:
                    x=a*100+b*10+c
                    if x>100:
                        print(x,end=' ')
else:
    print('illegal input')

