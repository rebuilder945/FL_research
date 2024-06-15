def wcnm(a):
    a=float(a)
    if a<20:
        b=6*a**2+1
    elif a>=40:
        b=100/(a+1)
    else:
        b=(3*a-60)**0.5
    return b
a=input()
print("%.2f"%wcnm(a))
