def f(x):
    if x<20:
        m=6*(x**2)+1
        print("%.2f"%m)
    elif 20<= x <40:
        m=(3*x-60)**0.5
        print("%.2f"%m)
    else:
        m=100/(x+1)
        print("%.2f"%m)
n=eval(input())
f(n)
