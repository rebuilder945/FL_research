x=eval(input())
def f(x):
    if x<20:
        a=6*x*x+1
        return a
    elif 20<=x<40:
        b=(3*x-60)**0.5
        return b
    elif x>=40:
        c=100/(x+1)
        return c
print("%.2f"%f(x))
