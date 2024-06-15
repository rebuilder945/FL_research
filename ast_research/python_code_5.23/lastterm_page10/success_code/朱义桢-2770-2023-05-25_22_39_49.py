def bianwei(n,m):
    if len(n)!=len(m):
        return(False)
    else:
        n=" ".join(n)
        m=" ".join(m)
        n=n.split()
        m=m.split()
        n.sort()
        m.sort()
        if n==m:
            return(True)
        else:
            return(False)
a=input()
b=input()
print(bianwei(a,b))
