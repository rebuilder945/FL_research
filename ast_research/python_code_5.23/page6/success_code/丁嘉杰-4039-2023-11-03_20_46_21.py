x=float(input())
if x<20:
    f=6*x**2+1
elif 40<=x:
    f=100/(x+1)
else:
    f=(3*x-60)**0.5
print("%.2f"%f)
