def f(x):
    if x < 20:
        a = 6*x*x+1
        return eval("%.2f"%a)
    if 20 <= x < 40:
        a = (3*x-60)**(1/2)
        return eval("%.2f"%a)
    a = 100/(x+1)
    return eval("%.2f"%a)
x = eval(input())
print(f(x))
