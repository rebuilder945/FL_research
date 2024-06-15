def f(x):
    if x < 20:
        a = 6*x*x+1
        return a
    if 20 <= x < 40:
        a = (3*x-60)**(1/2)
        return a
    a = 100/(x+1)
    return a
x = eval(input())
print("%.2f"%f(x))
