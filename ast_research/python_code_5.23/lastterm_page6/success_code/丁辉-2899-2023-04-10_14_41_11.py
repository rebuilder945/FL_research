from itertools import*
n,m=eval(input())
if n<m-2:
    a=list(permutations(range(n,m),3))
    b=" ".join(map(str,a))
    print(b)
