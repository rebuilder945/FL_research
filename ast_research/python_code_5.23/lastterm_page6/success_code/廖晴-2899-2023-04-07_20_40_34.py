n,m=map(int,input().split())
if n>=m or n<0 or m-n<3:
    print("illegal input")
else:
    if n==0:
        for a in range(1,m):
            for b in range(1,m):
                if b!=a:
                    s1=a*100+b*10
                    s2=a*100+b
                    print(s1,s2,end="")
    else:
        for a in range(n,m):
            for b in range(n,m):
                if b!=a:
                    for c in range(n,m):
                        if c!=b and c!=a:
                            s=a*100+b*10+c
                            print(s,end=" ")
