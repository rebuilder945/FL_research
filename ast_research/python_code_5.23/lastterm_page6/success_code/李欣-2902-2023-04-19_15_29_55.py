def duo(x):
    n=2
    m=1
    total=0
    while x>0:
        total+=n/m
        n+=m
        m=n-m
        x+=-1
    print("%.4f"%total)
n=input()
duo(n)
