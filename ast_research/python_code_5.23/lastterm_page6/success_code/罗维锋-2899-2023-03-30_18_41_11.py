import itertools
n,m=input().split("")
if m>=3:
    if n>=m and m-n<3:
        print("illegal input")
    else:
        c=[]
        a=list(range(n,m))
        b=list(itertools.permutations(a,3))
        for x in b:
            c.append(",".join(map(str,x)))
        print(" ".join(c))

