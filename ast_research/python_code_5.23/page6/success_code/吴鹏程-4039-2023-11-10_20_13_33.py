x=eval(input())
if x<20:
    x=6*x**2+1
elif 20<=x<40:
    x=(3*x-60)**0.5
elif x>=40:
    x=100/(x+1)
print("%.2f"%(x))
