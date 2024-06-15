def function(x):
    if x<20:
        print("%.2f"%(6*x*x+1))
    elif x>=20 and x<40:
        a=(3*x-60)**(1/2)
        print("%.2f"%(a))
    else:
        print("%.2f"%(100/(x+1)))
x=eval(input())
function(x)            


