def f(x):
    if x<20:
        return 6*x**2+1
    elif x>=40:
        return 100/(x+1)
    else:
        return (3*x-60)**(1/2)
x = eval(input())
print(f"{f(x):.2f}")

