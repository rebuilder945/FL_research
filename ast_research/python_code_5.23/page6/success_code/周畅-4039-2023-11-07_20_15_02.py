def inma(x):
    if x<20:
        a=6*x**2+1
    elif 20<=x<40:
        a=(3*x-60)**(1/2)
    elif x>=40:
        a=100/(x+1)
    print("%.2f"% a)
x=eval(input())
print(inma(x))
