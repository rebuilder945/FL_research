from itertools import*
n,m=map(int,input().split())
if n<m-2:
    a=list(permutations(range(n,m),3))
    b=" ".join(map(str,a))
    print(b)
