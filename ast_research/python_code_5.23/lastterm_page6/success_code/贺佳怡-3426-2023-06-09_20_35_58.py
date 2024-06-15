def f(a):
    import math
    if a<20:
        return (6*a**2+1)
    elif 20<=a<40:
        return  (math.sqrt(3*a-60))
    elif a>=40:
        return  (100/(a+1))
x=float(input())
print("%.2f" % f(x))

