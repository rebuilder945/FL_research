x=eval(input())
if x<20:
    t=6*x*x+1
if 20<=x<40:
    t=(3*x-60)**(1/2)
if x>=40:
    t=100/(x+1)
print("%.2f"%t)            
