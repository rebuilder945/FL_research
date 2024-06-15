x=eval(input())
if x<20:
    y=6*x**2+1
if 20<=x<40:
    y=(3*x-60)**0.5
if x>=40:
    y=100/(x+1)
print("%.2f"%y)
