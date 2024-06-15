x=eval(input())
def f(x):
    if x<20:
        return 6*x*x+1
    elif 20<=x<40:
        return (3*x-60)**0.5
    elif x>=40:
        return 100/(x+1)
print("%.2f"%(f(x)))
