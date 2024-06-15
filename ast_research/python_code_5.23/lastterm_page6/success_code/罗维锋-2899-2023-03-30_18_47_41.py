import itertools
n,m=input().split(" ")
n=int(n)
m=int(m)
if m>=3:
    if n>=m and m-n<3:
        print("illegal input")
    else:
        c=[]
        a=list(range(n,m))
        b=list(itertools.permutations(a,3))
        for x in b:
            c.append("".join(map(str,x)))
        c=list(map(int,c))
        while 0 in c:
            c.remove(0)
        c=list(map(str,c))
        print(" ".join(c))

