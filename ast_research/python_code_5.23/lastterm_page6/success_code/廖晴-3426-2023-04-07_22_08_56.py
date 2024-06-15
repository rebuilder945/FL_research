def f(i):
    if i<20:
        f=6*i*i+1
    elif i>=20 and i<40:
        f=pow(3*i-60,1/2)
    else:
        f=100/(i+1)
    return f
x=eval(input())
print("%.2f"%f(x))
