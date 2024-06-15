x=eval(input())
if x<20:
    y=6*x**2+1
if x>=20 and x<40:
    y=(3*x-60)**(1/2)
if x>=40:
    y=100/(x+1)
print("%.2f"%y)
