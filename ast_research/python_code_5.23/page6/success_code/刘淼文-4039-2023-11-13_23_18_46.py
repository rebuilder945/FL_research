x = eval(input())
if x<20:
    y = 6*x**2+1
elif 20<=x<40:
     y = (3*x-60)**(1/2)
else:
    y = 100/(x+1)
print("%.2f"%x)    
