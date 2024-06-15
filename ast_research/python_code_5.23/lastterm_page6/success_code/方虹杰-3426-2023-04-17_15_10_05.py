x=int(input())
if x<20:
    y=6*x**2+1
    print("%.2f"%(y))
elif x>=40:
    print("%.2f"%(100/(x+1)))
else:
    print("%.2f"%((3*x-60)**0.5))
