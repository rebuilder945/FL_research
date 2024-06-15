def fx(x):
    if x<20:
        y=6*x**2+1
    elif 20<=x<40:
        y=(3*x-60)**0.5
    elif x>=40:
        y=100/(x+1)
    return(y)

a=eval(input())
b=fx(a)
print("%.2f"%(b))
