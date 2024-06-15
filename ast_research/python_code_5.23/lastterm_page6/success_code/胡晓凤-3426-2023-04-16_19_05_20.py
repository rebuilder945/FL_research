x=eval(input())
if x <20:
    m=6*x**2+1
elif 20<=x<40:
    m=(3*x-60)**(1/2)
elif x>=40:
    m=100/(x+1)
print ("%.2f"%m)
