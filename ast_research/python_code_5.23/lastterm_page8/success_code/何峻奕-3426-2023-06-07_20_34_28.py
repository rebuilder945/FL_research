x=eval(input())
if x<20:
    c=6*x**2+1
if 20<=x<40:
    c=(3*x-60)**(1/2)
if x>=40:
    c=100/(x+1)
print("%.2f"%c)
