x=float(input())
if x<20:
    s=6*x*x+1
elif x>=20 and x<40:
    s=(3*x-60)**0.5
else:
    s=100/(x+1)
print("%.2f"%s)
