n,m=1,4
e=[]
if n>m:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    d=a*100+b*10+c
                    e.append(d)
    print(e)
else:
    print("illegal input")



