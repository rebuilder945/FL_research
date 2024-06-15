from math import*
def f1(x):
    return 6*X*X+1
def f2(x):
    return sqrt(3*x-60)
def f3(x):
    return 100/(x+1)
x=eval(input())
if x<20:
    print("{:.2f}".format(f1(x)))
elif 20<=x<40:
    print("{:.2f}".format(f2(x)))
else:
    print("{:.2f}".format(f3(x)))
