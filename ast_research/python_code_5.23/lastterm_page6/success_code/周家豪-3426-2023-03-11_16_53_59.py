def function(x):
    if x<20:
        num=6*x**2+1
    elif 20<=x<40:
        num=(3*x-60)**0.5
    elif x >=40:
        num=100/(x+1)
    return num

x=eval(input())
print("%.2f"%(function(x)))
