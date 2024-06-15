n,m=map(int,input().split())
b=[]
if 0<=n<m<=9 and m-n>=3 and int(m)==m and n==int(n):
    for i in range(n,m):
        for j in range(n,m):
            for h in range(n,m):
                if i!=j and i!=h and j!=h:
                    a=100*i+10*j+h
                    if a>99:
                        b.append(a)

    c=list(map(str,b))
    print(" ".join(c))
else:
    print("illegal input")

