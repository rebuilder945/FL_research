def f(x):
    m=0
    if x<20:
        m+=6*x**2+1
        return m
    elif 20<=x<40:
        m+=(3*x-60)**0.5
    else:
        m+=100/(x+1)
n=eval(input())
print("%.2f"%(f(n)))
