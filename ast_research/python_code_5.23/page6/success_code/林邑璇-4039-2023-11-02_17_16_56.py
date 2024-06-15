import math
def hanshu(x):
    if x<20:
        a=6*x*x+1
    elif 19<x<40:
        a=math.sqrt(3*x-60)
    else:
        a=100/(x+1)
    print("%.2f"%a)
x=eval(input())
hanshu(x)
