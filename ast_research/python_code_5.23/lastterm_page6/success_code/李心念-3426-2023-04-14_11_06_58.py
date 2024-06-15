x = eval(input())
def f1(n):
    a = 6*n*n+1
    return round(2,a)
def f2(n):
    a = (3*n-60)**(0.5)
    return round(2,a)
def f3(n):
    a = 100/(n+1)
    return round(2,a)
if x < 20:
    print(f1(x))
elif 20<= x <40:
    print(f2(x))
else:
    print(f3(x))
