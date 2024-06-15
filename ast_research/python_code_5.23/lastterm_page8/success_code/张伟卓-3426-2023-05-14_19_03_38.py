def fx(x):
    if x<20:
        fx=6*x**2+1
    elif 20<=x<40:
        fx=(3*x-60)**0.5
    elif x>=40:
        fx=100/(x+1)
    return fx
n=eval(input())
print("%.2f"%fx(n))
