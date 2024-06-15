

x=eval(input())
if x>=40:
    c=100/(x+1)
    print("%.2f"%c)
elif x<20:
    c=6*(x**2)+1
    print("%.2f"%c)
elif x>=20 and x<40:
    c=(3*x-60)**(1/2)
    print("%.2f"%c)
