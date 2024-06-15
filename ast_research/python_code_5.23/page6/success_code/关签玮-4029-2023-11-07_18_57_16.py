n,m=map(int,input().split())
if m-n>=3 and n>0 and m>0:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a:
                    d=a*100+b*10+c
                    if d>99:
                        print(d,end=" ")
else:
    print("illegle input")

