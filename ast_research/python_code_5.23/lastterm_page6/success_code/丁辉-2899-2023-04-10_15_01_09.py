from itertools import*
n,m=map(int,input().split())
if n<m-2 and m<=10 and n>=0:
    a=list(permutations(range(n,m),3))
    b=[]
    c=[]
    for i in a:
        b.append(str(i[0])+str(i[1])+str(i[2]))
    for i in range(len(b)):
        if b[i][0]!=0:
            c.append(b[i])
    print(" ".join(c))
else:
    print("illegal input")
