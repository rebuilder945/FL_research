def f(x):
    if x<20:
        return 6*x*x+1
    elif 20<=x<40:
        return pow(3*x-60,0.5)
    else:
        return 100/(x+1)
x=eval(input())
print("%.2f"%f(x))
