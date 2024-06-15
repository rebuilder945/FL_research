def f(x):
    if x<20:
        f(x)=x**2*6+1
    elif x<40:
        f(x)=pow((x*3-60),0.5)
    else:
        f(x)=100/(x+1)
x=eval(input())
print("%.2f"%f(x))

