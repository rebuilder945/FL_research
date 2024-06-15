def f(x):
    if x<20:
        return x*x*6+1
    elif 20<=x<=40:
        return (3*x-60)**0.5
    elif x>40:
        return 100/(x+1)
x=eval(input())
eva=f(x)
print("%.2f"%eva)

