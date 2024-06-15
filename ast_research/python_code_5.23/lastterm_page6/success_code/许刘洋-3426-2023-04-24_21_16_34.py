x=eval(input())
def f(x):
    if x <20:
        out=6*x**2+1
    elif 20<=x<40:
        out=(3*x-60)**0.5
    elif x>=40:
        out=100/(x+1)
    return(out)
print("%.2f"%f(x))
