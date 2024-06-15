def f1(x):
    return x**2*6+1
def f2(x):
    return (x*3-60)**0.5
def f3(x):
    return 100/(x+1)
x=eval(input())
if x<20:
    print("%.2f"%f1(x))
elif 20<=x<40:
    print("%.2f"%f2(x))
else:
    print("%.2f"%f3(x))
