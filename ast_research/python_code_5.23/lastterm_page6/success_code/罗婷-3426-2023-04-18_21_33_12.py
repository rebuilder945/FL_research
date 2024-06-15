a=eval(input())
s=0
if a<20:
    s=float(6*a**2+1)
elif a>=20 and a<40:
    s=(3*a-60)**0.5
elif a>=40:
    s=float(100/(a+1))
print("%.2f"%s)
