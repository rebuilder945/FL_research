x=eval(input())
if x <20:
    r=6*(x**2)+1
elif x>=20 and x<40:
    r=(3*x-60)**(1/2)
else:
    r=100/(x+1)
print("%.2f"%r)
