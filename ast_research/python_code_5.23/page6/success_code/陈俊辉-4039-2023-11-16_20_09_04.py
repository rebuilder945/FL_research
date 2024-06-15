x=input()
if x<20:
    x=6*x**2+1
elif 20<=x<40:
    x=(3*x-60)**0.5
elif 40<=x:
    x=100/(x+1)
print(x)
