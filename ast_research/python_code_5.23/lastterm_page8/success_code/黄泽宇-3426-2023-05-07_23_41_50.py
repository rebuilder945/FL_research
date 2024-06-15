def op(x):
    if x<20:
        x=1+6*x**2
    elif x>=20 and x<40:
        x=(3*x-60)**0.5
    else:
        x=100/(x+1)
    return x
a=eval(input)
c=op(a)
print("%.2f"%(c))
