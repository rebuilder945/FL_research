x=eval(input())
if x<20:
    fx=6*x**2+1
    print("%.2f"%fx)
elif 20<=x<=40:
    fx=(3*x-60)**(1/2)
    print("%.2f"%fx)
else:
    fx=100/(x+1)
    print("%.2f"%fx)
