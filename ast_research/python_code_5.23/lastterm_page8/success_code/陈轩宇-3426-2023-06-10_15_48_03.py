def hanshu(x):
    if x<20:
        jiguo = 6*x**2+1
    elif x>=20 and x<40:
        jiguo = (3*x-60)**(1/2)
    else:
        jiguo = 100/(x+1)
    return jiguo

x = eval(input())
print("%.2f"%hanshu(x))
