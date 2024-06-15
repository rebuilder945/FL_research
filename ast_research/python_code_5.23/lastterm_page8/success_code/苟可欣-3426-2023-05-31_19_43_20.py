x=eval(input())
if x<20:
    k=6*x**2+1
elif x>=40:
    k=100/(x+1)
else:
    k=(3*x-60)**(1/2)
print("%.2f"%(k))
