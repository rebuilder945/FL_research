x=eval(input())
def f(x):
    if x<20:
        print("%.2f"%(6*(x**2)+10))
    elif 20<=x<40:
        print("%.2f"%((3*x-60)**0.5))
    else:
        if x>=40:
            print("%.2f"%(100/(x+1)))
f(x)
