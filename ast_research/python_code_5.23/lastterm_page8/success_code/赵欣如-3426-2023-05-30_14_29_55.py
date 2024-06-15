import math
def f(x):
    if x<20:
        return(6*(x**2)+1)
    if x>=20 and x<40:
        return(math.sqrt(3*x-60))
    if x>=40:
        return(100/(x+1))
n=float(input())
print("%.2f"%f(n))
