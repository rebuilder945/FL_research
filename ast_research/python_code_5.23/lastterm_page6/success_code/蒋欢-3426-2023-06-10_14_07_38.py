def hanshu(x):
    if x<20:
        print("%.2f"%(6*x**2+1))
    elif x<40:
        print("%.2f"%((3*x-60)**0.5))
    elif x>=40:
        print("%.2f"%(100/(2*x+1)))
x=eval(input())
hanshu (x)
