from math import sqrt
def function(x):
    if x<20:
        return 6*x*x+1
    elif x<40:
        return sqrt(3*x-60)
    else:
        return 100/(x+1)

x=eval(input())
print("%.2f"%(function(x)))
