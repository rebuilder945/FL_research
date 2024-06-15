x = eval(input())
if x<20:
    a = 6*x**2+1
    print("%.2f"%a)
elif 20<=x<40:
    a = (3*x-60)**(1/2)
    print("%.2f"%a)
else:
    a = 100/(x+1)
    print("%.2f"%a)
