x=eval(input())
if x<20:
    x=6*x**2+1
if 20<=x<40:
    x=(3*x-60)**0.5
if x>=40:
    x=100/(x+1)
print("%.2f"%(x))
