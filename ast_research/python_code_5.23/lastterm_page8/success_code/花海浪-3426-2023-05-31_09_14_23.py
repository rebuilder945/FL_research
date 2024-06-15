x=eval(input())
if x<20:
    print("%.2f"%(x**2*6+1))
elif 20<=x<40:
    print("%.2f"%((x*3-60)**0.5))
else:
    print("%.2f"%(100/(x+1)))
