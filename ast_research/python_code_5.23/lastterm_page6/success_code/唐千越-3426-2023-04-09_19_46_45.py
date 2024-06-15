def f(x):
    if x<20:
        f = 6*x^2+1
    if x>=20 and x <40:
        f = (3*x-60)^0.5
    if x>=40:
        f = 100/(x+1)
    print("%.2f"%(f))
f(x)
print(x)
