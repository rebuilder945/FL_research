x=eval(input())
if x<20:
    print("%.2f"%(x*x*6+1))
if x<40 and x>=20:
    print("%.2f"%((3*x-60)**1/2))
else:
    print("%.2f"%(100/(x+1)))
