def f(x):
    if x<20:
        return 6*x**2+1
    elif x<40:
        return (3*x-60)**(1/2)
    else:
        return 100/(x+1)
x=eval(input())
print("%.2f"%f(x))
