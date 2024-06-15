x=eval(input())
def f(x):
    if x<20:
        return 6*pow(x,2)+1
    elif 20<=x<40:
        return pow(3*x-60,0.5)
    else:
        return 100/(x+1)
print("{:.2f}".format(f(x)))
