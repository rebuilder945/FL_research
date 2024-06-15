def f(x):
    if x < 20:
        N = 6 *x*x +1
    elif x < 40:
        N = (3*x-60)**(1/2)
    elif x>=40:
        N = 100/(x+1)
    print("%.2f"%(N))
x = eval(input())
f(x)
