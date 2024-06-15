x=eval(input())
if x < 20:
    b=6*x**2+1
    print("%.2f"%b)
elif 20<=x<40:
    b=3*x-60
    c=b**0.5
    print("%.2f"%c)
else:
    b=x+1
    c=100/b
    print("%.2f"%c)
