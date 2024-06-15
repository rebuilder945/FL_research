x = eval(input())
if x<20:
    n = 6*x*x+1
    print("%.2f"%(n))
elif 20<=x<40:
    n = (3*x-60)**0.5
    print("%.2f"%(n))
else:
    n = 100/(x+1)
    print("%.2f"%(n))
