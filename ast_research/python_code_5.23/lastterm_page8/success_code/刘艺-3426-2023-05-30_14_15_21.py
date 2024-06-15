a = eval(input())
if a < 20:
    m = 6*a**2+1
    print("%.2f"%(m))
if 20<=a<40:
    m = (3*a-60)**0.5
    print("%.2f"%(m))
if a>=40:
    m = 100/(a+1)
    print("%.2f"%(m))
