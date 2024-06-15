def f(x):
    if x < 20:
        f(x)==6*x*x + 1
    elif 20 <= x < 40:
        f(x)==(3*x-60)**(1/2)
    else:
        f(x)==100/(x+1)
    return f(x)

x=input()
print(f"{f():.2f}")
