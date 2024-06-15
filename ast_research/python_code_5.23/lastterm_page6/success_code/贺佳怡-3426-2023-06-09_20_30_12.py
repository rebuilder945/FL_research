def f(a):
    import math
    if a<20:
        print("%.2f" % (6*a**2+1))
    elif 20<=a<40:
        print("%.2f" % (math.sqrt(3*a-60)))
    elif a>=40:
        print("%.2f" % (100/(a+1)))

