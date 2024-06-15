import itertools
n,m=input().split(" ")
n=int(n)
m=int(m)
if m>=3 and m<=10:
    if n>=m or m-n<3:
        print("illegal input")
    else:
        c=[]
        d=[]
        a=list(range(n,m))
        b=list(itertools.permutations(a,3))
        for x in b:
            c.append("".join(map(str,x)))
        for i in range(len(c)):
            if c[i][0]!='0':
                d.append(c[i])
        print(" ".join(d))
else:
    print("illegal input")
