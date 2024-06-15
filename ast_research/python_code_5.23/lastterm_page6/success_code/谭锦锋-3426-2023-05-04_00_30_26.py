def f1(x):
    return 6*x**2+1
def f2(x):
    return (3*x-60)**1/2
def f3(x):
    return 100/(x+1)
n = eval(input())
if n <20:
    print("%.2f"%f1(n))
elif 20<=n<=40:
    print("%.2f"%f2(n))
else:
    print("%.2f"%f3(n))
