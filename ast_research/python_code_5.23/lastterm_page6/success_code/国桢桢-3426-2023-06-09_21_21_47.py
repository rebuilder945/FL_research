x= eval(input())
def f(x):
    if x <20:
        return 6*x*x+1
    if 20<=x<40:
        return (3*x-60)**0.5
    if x>=40:
        return 100/(x+1)
y = f(x)
print("%.2f"%(y))
