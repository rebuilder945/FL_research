from math import sqrt
x=eval(input())
fx=0
if x<20:
    fx=6*x**2+1
elif 20<=x<40:
    fx=sqrt(3*x-60)
else:
    fx=100/(x+1)
print("%.2f"%fx)
