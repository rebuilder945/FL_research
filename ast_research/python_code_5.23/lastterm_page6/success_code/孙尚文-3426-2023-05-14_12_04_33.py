def hanshu(x):
    if x<20:
        b=6*x**2+1
        print("%.2f"%(b))
    if 20<=x<40:
        c=(3*x-60)**0.5
        print("%.2f"%(c))
    if x>=40:
        d=100/(x+1)
        print("%.2f"%(d))
x=eval(input())
hanshu(x)
