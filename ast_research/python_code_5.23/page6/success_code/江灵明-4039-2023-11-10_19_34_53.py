x = eval(input())
def f(x):
    N=0
    if x<20:
        N=6*x**2
    if 20<=x<40:
        N=(3*x-60)**0.5
    if x>=40:
        N = 100/(x+1)
    print("%.2f"%N)
f(x)
