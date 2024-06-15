p=list(map(int,input().split()))
n,m=p[0],p[1]
if n<m and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a: 
                    x=a*100+b*10+c
                    if x>100:
                        print(x,end=" ")
else:print("illegal input")

