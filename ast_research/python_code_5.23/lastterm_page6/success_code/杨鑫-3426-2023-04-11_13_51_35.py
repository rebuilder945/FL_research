x=eval(input())
b=0
if x<20:
    b=6*x**2+1
elif 20<=x<40:
    b=(3*x-60)**0.5
elif 40<=x:
    b=100/(x+1)
print("%.2f"%b)
