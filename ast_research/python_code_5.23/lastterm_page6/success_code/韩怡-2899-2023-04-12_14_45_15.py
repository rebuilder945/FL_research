a=input().split()
n=int(a[0])
m=int(a[1])
if n>=m-2 or min(n,m)<0 or max(n,m)>=10:
    print("illegal input")
else:
    c=[p for p in range(n,m)]
    for t in range(len(c)):
        x=int(c[t])
        for k in range(len(c)):
            y=int(c[k])
            for l in range(len(c)):
                z=int(c[l])
                if x!=y and x!=z and y!=z and x!=0:
                    print(100*x+10*y+z,end=" ")
                else:
                    pass
