x = eval(input())
if x<20:
    f = 6*x**2+1
elif 20<=x<40:
    f = (3*x-60)**(1/2)
else:
    f = 100/(x+1)
print("%.2f"%f)
