def f(x):
    if x<20:
        return (6*(x**2))+2
    elif 20<=x<40:
        return (3*x-60)**1/2
    elif x>=40:
        return 100/(x+1)
num=eval(input())
print("%.2f"%f(num))
