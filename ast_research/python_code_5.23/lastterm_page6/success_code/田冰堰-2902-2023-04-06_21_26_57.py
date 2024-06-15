def f(n):
    a=2
    b=1
    total=0
    for i in range(1,n+1):
        a,b=a+b,a
        print(f(n))
