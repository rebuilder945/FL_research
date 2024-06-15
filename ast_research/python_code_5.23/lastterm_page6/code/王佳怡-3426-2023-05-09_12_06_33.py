def f(x):
    if x<20:
        f(x)=x**2*6+1
    elif 20<=x<40:
        import math
        f(x)=math.sqrt(x*3-60)
    else:
        f(x)=100/(x+1)
x=eval(input())
print("%.2f"%f(x))

