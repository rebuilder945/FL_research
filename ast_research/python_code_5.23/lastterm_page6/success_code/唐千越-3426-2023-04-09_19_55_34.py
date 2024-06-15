import math
def f(x):
    if x<20:
        f = 6*x^2+1
        print("%.2f"%(f))
    if x>=20 and x <40:
        f = math.sqrt(3*x-60)
        print("%.2f"%(f))
    if x>=40:
        f = 100/(x+1)
        print("%.2f"%(f))
x=eval(input())
f(x)
print(x)
