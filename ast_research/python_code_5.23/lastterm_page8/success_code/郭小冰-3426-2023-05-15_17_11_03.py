def f(x):
    if x<20:
        return 6*x*x+1
    elif x<40 and x>=20:
        return(3*x-60)**(1/2)
    elif x>=40:
        return 100/(x+1)
a=eval(input())
eval=f(a)
print("%.2f"%eval)
