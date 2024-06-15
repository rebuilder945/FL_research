x = eval(input())
if x<20:
    y = 6*x**2+1
    print("{:.2f}".format(y))
elif 20<=x<40:
    y = (3*x-60)**(1/2)
    print("%.2f"%(y))
else:
    y = 100/(x+1)
    print("%.2f"%(y))
