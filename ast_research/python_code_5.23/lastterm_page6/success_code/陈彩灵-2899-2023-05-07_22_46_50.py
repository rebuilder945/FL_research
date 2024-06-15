n,m=input().split(' ')
n=int(n)
m=int(m)
if 0<=n<m<11 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    N=a*100+b*10+c
                    if N>90:
                        print(N,end=' ')
else:
    print('illegal input')
        
