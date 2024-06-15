def f(x):
    if x<20:
        z = x^2
        y = 6*(z)+1
    elif x>=20 and x<40:
        z = 3*x
        y = (z-60)^0.5
    else:
        y=100/(x+1)
    return y
x = eval(input())
y = f(x)
print("%.2f"%(y))
