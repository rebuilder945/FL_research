from itertools import*
n,m=map(int,input().split())
if n<m-2:
    a=list(permutations(range(n,m),3))
    b=[]
    for i in a:
        b.append(str(i[0])+str(i[1])+str(i[2]))
    c=" ".join(b)
    print(c)

